import discord

def etiqueta_reducir():
    embed = discord.Embed(
        title = 'Redución el desperdicio alimentario',
        description = 'Descubre como reducir la cantidad de residuos organicos en casa',
        color = 0xA9C46C
    )
    embed.add_field(
        name = 'Consejo 1: Planifica tus comidas',
        value = 'Puedes tener en cuenta cuantas personas hay en tu cas y cuanto comen, sin olvidar de una buena lista de compras',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 2: Comprueba la caducidad de tus alimentos',
        value = 'Dale prioridad a los alimentos que estén a punto de caducar y asegurate de verificar su fecha de caducidad antes de comprarlos',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 3: Ajusta la temperatura de la nevera. ..',
        value = 'La nevera debe estar a 4ºC, y las puertas y cajones siempre bien cerrados',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 4: Respeta las indicaciones de conservación de los alimentos',
        value = 'Respeta las indicaciones sobre conservación presentes en el envase, tanto para los alimentos que necesitan frío como para aquellos que no',
        inline = False
    )
    embed.set_thumbnail(url = 'https://i.postimg.cc/9FSpghq4/reciclage1.jpg')
    return embed

def etiqueta_separar_y_reciclar():
    embed = discord.Embed(
        title = 'Separar y reciclar desechos',
        description = 'Descubre como separar y reciclar los desechos en casa',
        color = 0xA9C46C
    )
    embed.add_field(
        name = 'Consejo 1: Lava los envases antes de reciclar',
        value = 'Antes de reciclar los envases, asegurate de lavarlos bien para evitar malos olores y la proliferación de insectos',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 2: Separa los residuos en casa',
        value = 'Separa los residuos en casa en diferentes contenedores para facilitar el proceso de reciclaje',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 3: Reutiliza los envases',
        value = 'Reutiliza los envases de plástico, vidrio y papel siempre que sea posible',
        inline = False
    )
    embed.set_thumbnail(url = 'https://i.postimg.cc/Y02ctQYd/reciclage2.jpg')
    return embed
   
   
def etiqueta_evitar_usode_plastico():
    embed = discord.Embed(
        title = 'Evitar el uso de bolsas y envases de plástico',
        description = 'Descubre como reducir el uso de bolsas y envases de plástico en casa',
        color = 0xA9C46C
    )
    embed.add_field(
        name = 'Consejo 1: Usa bolsas reutilizables',
        value = 'Usa bolsas reutilizables para hacer la compra y evita el uso de bolsas de plástico',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 2: Sustituye las pajitas de plástico por las de metal',
        value = 'Sustituye las pajitas de plástico por las de metal o de papel para reducir el uso de plástico',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 3: Evita comprar productos envasados en plástico',
        value = 'Evita comprar productos envasados en plástico y opta por productos a granel o en envases de vidrio',
        inline = False
    )
    embed.set_thumbnail(url = 'https://i.postimg.cc/c1kkKqSx/reciclage4.jpg')
    return embed 

def etiqueta_hacer_compost_casero():
    embed = discord.Embed(
        title = 'Reutilizar los restos orgánicos como compost',
        description = 'Descubre como reutilizar los restos orgánicos para hacer compost en casa',
        color = 0xA9C46C
    )
    embed.add_field(
        name = 'Consejo 1: Separa los restos orgánicos',
        value = 'Separa los restos orgánicos de la basura y guárdalos en un recipiente especial para compost',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 2: Añade restos de poda y hojas secas',
        value = 'Añade restos de poda, hojas secas y otros materiales orgánicos para enriquecer el compost',
        inline = False
    )
    embed.add_field(
        name = 'Consejo 3: Remueve el compost regularmente',
        value = 'Remueve el compost regularmente para favorecer la descomposición de los restos orgánicos',
        inline = False
    )
    embed.set_thumbnail(url = 'https://i.postimg.cc/2S7KS1jJ/reciclage5.jpg')
    return embed

    
    