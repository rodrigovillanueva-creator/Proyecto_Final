import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

puntos = {}

pregunta_actual = {}

RETOS = [
    "Usa una botella reutilizable en lugar de comprar una de plástico.",
    "Lava los platos o frutas usando un recipiente con agua.",
    "Lleva tu propia bolsa de tela o mochila si vas a comprar.",
    "Rechaza sorbetes o cubiertos de plástico si pides comida.",
    "Apaga las luces y desconecta los aparatos que no estés usando.",
    "Toma una ducha rápida de 5 minutos.",
    "Separa en casa los residuos reciclables de la basura común.",
    "Intenta que una de tus comidas sea basada en vegetales.",
    "Aprovecha la luz natural del día antes de encender focos."
]
# Diccionario con los factores de emisión por kilómetro

Produccion_CO2 = {
    "auto": 0.19,
    "bus": 0.05,
    "metro": 0.03,
    "bici": 0.0,
    "caminando": 0.0
}
# Diccionario de Trivias


PREGUNTAS = [
    """❓ ¿Qué produce más CO2 en el mundo?
A) Combustibles fósiles
B) Volcanes
C) Respirar""",

    """❓ ¿Cuál transporte contamina MENOS por persona?
A) Auto particular
B) Bicicleta o caminar
C) Avión""",

    """❓ ¿Qué le pasa al mar si absorbe mucho CO2?
A) Se vuelve dulce
B) Se acidifica y daña los corales
C) No le pasa nada"""
]

# --- LISTA DE RESPUESTAS ---
RESPUESTAS = [
    "a",
    "b",
    "b"
]


def calcular_co2(medio, km):
    medio_limpio = medio.lower()

    if medio_limpio in Produccion_CO2:
        emision = km * Produccion_CO2[medio_limpio]
        return round(emision, 2)
    else:
        return None


@bot.event
async def on_ready():
    print(f'¡El bot está en línea y conectado como {bot.user}!')
    channel = discord.utils.get(bot.get_all_channels(), name="general")
    await channel.send(
            "🌱 **¡Hola! Soy tu bot de sostenibilidad.**\n\n"
            "Para usar el bot, aquí tienen los comandos principales:\n"
            "• **!reto** - Recibe un reto ecológico del día.\n"
            "• **!cumplido** - Reclama +10 puntos al terminar tu reto.\n"
            "• **!trivia** - Responde una pregunta sobre el medio ambiente.\n"
            "• **!respuesta <a/b/c>** - Responde a la trivia activa.\n"
            "• **!huella <medio> <km>** - Calcula tu emisión de CO2.\n"
            "• **!mispuntos** - Revisa cuántos puntos acumulaste.")


@bot.command()
async def reto(ctx):
    elegido = random.choice(RETOS)
    await ctx.send(f"🌱 Tu reto del día:"
                   f"¡{elegido}!\n(Escribe !cumplido cuando lo termines)")


@bot.command()
async def cumplido(ctx):
    usuario = ctx.author.name

    if usuario not in puntos:
        puntos[usuario] = 0

    puntos[usuario] = puntos[usuario] + 10
    await ctx.send(f"🎉 ¡Bien hecho {usuario}! "
                   f"Ganaste +10 puntos por cumplir el reto.")


@bot.command()
async def trivia(ctx):
    usuario = ctx.author.name
    pregunta_elegida = random.choice(PREGUNTAS)

    pregunta_actual[usuario] = pregunta_elegida

    await ctx.send(f"{pregunta_elegida}, "
                   f"Responde escribiendo: !respuesta a (o b/c)")


@bot.command()
async def respuesta(ctx, tu_respuesta: str = None):
    usuario = ctx.author.name

    if usuario not in pregunta_actual:
        await ctx.send("❌ Primero pide una pregunta escribiendo !trivia")
        return

    if tu_respuesta is None:
        await ctx.send("❌ Escribe tu respuesta. Ejemplo: !respuesta a")
        return

    pregunta = pregunta_actual[usuario]
    tu_respuesta = tu_respuesta.lower()

    es_correcta = False
    if "Combustibles fósiles" in pregunta and tu_respuesta == "a":
        es_correcta = True
    elif "Bicicleta o caminar" in pregunta and tu_respuesta == "b":
        es_correcta = True
    elif "Se acidifica" in pregunta and tu_respuesta == "b":
        es_correcta = True

    if es_correcta:
        if usuario not in puntos:
            puntos[usuario] = 0
        puntos[usuario] = puntos[usuario] + 10
        await ctx.send(f"✅ ¡Correcto {usuario}! Ganaste +10 puntos.")
    else:
        await ctx.send(f"❌ Respuesta incorrecta {usuario}. ¡Sigue intentando!")


@bot.command()
async def huella(ctx, medio: str = None, km: float = None):
    if medio is None or km is None:
        await ctx.send(
            "❌ Uso correcto: !huella <medio> <km>. Ejemplo: !huella auto 10"
        )
        return

    resultado = calcular_co2(medio, km)
    if resultado is None:
        await ctx.send(
            "❌ Usa un medio válido: auto, bus, metro, bici o caminando."
        )
    else:
        await ctx.send(
            f"📊 Recorrer {km} km en {medio} generó un estimado de "
            f"{resultado} kg de CO2."
        )


@bot.command()
async def mispuntos(ctx):
    usuario = ctx.author.name
    if usuario in puntos:
        total = puntos[usuario]
    else:
        total = 0
    await ctx.send(f"🏆 {usuario}, tienes {total} puntos acumulados.")

bot.run("MTQ1MTk3MTQwNDI5MDU4ODcxNA."
        "G5a4TT.VW2IKCTjLp5dKeLHPCww"
        "SUcvUye8kFWgzU6Bfs")
