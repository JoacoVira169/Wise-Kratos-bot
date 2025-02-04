import discord

def etiqueta_reducir():
    embed = discord.Embed(
        title = 'Redución el desperdicio alimentario',
        description = 'Descubre como reducir la cantidad de residuos organicos en casa',
        color = 0xA9C46C
    )
    embed.add_field(
        name = 'Consejo 1:',
        value = 'Esto es un consejo...',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 2:',
        value = 'Esto es un consejo...',
        inline = False
    )
    embed.set_thumbnail(url = 'https://i.postimg.cc/9FSpghq4/reciclage1.jpg')
    return embed