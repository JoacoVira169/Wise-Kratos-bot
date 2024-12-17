import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp as youtube_dl  # Usar yt-dlp en lugar de youtube_dl
from dotenv import load_dotenv
import logic as l

# Cargar token desde .env
load_dotenv()
token = os.getenv('DT')

# Intents y configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Opciones de yt-dlp
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # Evita problemas de IPv6
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

# Clase para manejar el audio descargado
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]  # Si es una playlist, toma el primer elemento

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# Comando: Unirse a un canal de voz
@bot.command()
async def join(ctx):
    if ctx.author.voice:  # Verifica si el usuario está en un canal de voz
        channel = ctx.author.voice.channel
        if not ctx.voice_client:  # Si no está conectado, se conecta
            await channel.connect()
            await ctx.send(f"🔊 Conectado a: {channel}")
        else:
            await ctx.send("⚠️ ¡Ya estoy conectado a un canal de voz!")
    else:
        await ctx.send("❌ ¡Debes estar en un canal de voz para que me conecte!")

# Comando: Desconectarse del canal de voz
@bot.command()
async def leave(ctx):
    if ctx.voice_client:  # Verifica si el bot está conectado
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Me desconecté del canal de voz.")
    else:
        await ctx.send("❌ No estoy conectado a ningún canal de voz.")

# Comando: Reproducir música desde YouTube
@bot.command(name="yt")
async def yt(ctx, *, url):
    # Verificar si el bot está conectado, si no, se conecta
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("❌ ¡Debes estar en un canal de voz para usar este comando!")
            return

    async with ctx.typing():  # Muestra el "bot escribiendo..."
        player = await YTDLSource.from_url(url, loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(f"Error: {e}") if e else None)

    await ctx.send(f"🎶 Reproduciendo ahora: **{player.title}**")

# Comando: Saludar
@bot.command()
async def hello(ctx):
    await ctx.send(f"👋 Hola, soy {bot.user}!")

# Comando: Generar "heh"
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

# Comando: Generar contraseña
@bot.command(name='password')
async def password(ctx, a=25):
    ctr = l.contra(a)
    await ctx.send(f"🔒 Tu contraseña es: `{ctr}`")

# Ejecutar el bot
bot.run(token)
