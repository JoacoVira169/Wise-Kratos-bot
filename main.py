import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp as youtube_dl  # Usar yt-dlp en lugar de youtube_dl
from dotenv import load_dotenv
import logic as l
import commandapi as ca, ambiente as am

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

@bot.command(name='meme')
async def mimi(ctx):
    img = l.meme()
    await ctx.send(file = img)

@bot.command(name='memes')
async def momos(ctx):
    img = l.memes()
    await ctx.send(file = img)
    
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = ca.duck_image()
    await ctx.send(image_url)
    
@bot.command(name = "anime")
async def anime(ctx, a):
    query = a
    anime_data = ca.get_anime_image(query)
    if anime_data:
        for anime in anime_data:
            
            image_url = anime['attributes']['posterImage']['small']
            await ctx.send(f"Image URL: {image_url}")
    else:
        await ctx.send("No se pudieron obtener datos de anime.")

@bot.command(name = "eco")
async def eco(ctx):
    menu = (
        "**🌍 ¿Qué quieres aprender hoy? 🌱**\n"
        "1️⃣ Reducción de residuos alimentarios\n"
        "2️⃣ Ideas para separar y reciclar\n"
        "3️⃣ Evitar el uso de bolsas de plástico\n"
        "4️⃣Reutilizar los restos organicos como compost \n\n"
        "Responde con el número de la opción que deseas conocer. ⬇️"
    )

    await ctx.send(menu)
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()
    try: 
        msg = await bot.wait_for('message', check = check, timeout = 10)
        opcion = int(msg.content)
        
        if opcion == 1:   
            await ctx.send(embed = am.etiqueta_reducir())
            
        elif opcion == 2:
            await ctx.send(embed = am.etiqueta_separar_y_reciclar()) 
            
        elif opcion == 3:
            await ctx.send(embed = am.etiqueta_evitar_usode_plastico())
            
        elif opcion == 4:
            await ctx.send(embed = am.etiqueta_hacer_compost_casero())
        
        else:
            await ctx.send('❌ Opción no válida. Intenta de nuevo.')
            
    except TimeoutError:
        await ctx.send('⏳ No respondiste a tiempo. Intenta de nuevo con `/eco`.')
          


# Ejecutar el bot
bot.run(token)
