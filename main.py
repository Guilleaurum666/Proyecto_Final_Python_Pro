import os
import discord
from discord.ext import commands
from analizador import AnalizadorClima

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
analizador = AnalizadorClima()


@bot.event
async def on_ready():
    print(f'✅ Bot conectado como: {bot.user}')


@bot.command(name='analizar')
async def analizar(ctx, *, contenido: str):
    res = analizador.procesar_entrada(contenido)
    
    mensaje = (
        f"📋 **ANÁLISIS DE CREDIBILIDAD**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• **Credibilidad:** {res['credibilidad']}\n"
        f"• **Riesgo de Greenwashing:** {res['riesgo']} ({res['porcentaje']}%)\n\n"
        f"📊 **Desglose:**\n"
        f"• **Datos reales:** {res['concretas']}\n"
        f"• **Palabras imprecisas / vanidad:** {res['vagas']}\n\n"
        f"💬 **Explicación:** {res['detalle']}"
    )
    await ctx.send(mensaje)


@bot.command(name='nube')
async def nube(ctx):
    ruta = analizador.generar_nube_palabras()
    if ruta and os.path.exists(ruta):
        await ctx.send(file=discord.File(ruta))
    else:
        await ctx.send("⚠️ No hay suficientes registros guardados para generar la nube.")


TOKEN = os.getenv('DISCORD_TOKEN', 'REEMPLAZAR_TOKEN_AQUI')
bot.run(TOKEN)