import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} conectado.')

@bot.command()
async def previsao(ctx):
    # Aqui entra o código de previsão
    prediction = "Skin XYZ"  # Você precisa desenvolver o algoritmo ou método para prever
    await ctx.send(f'Previsão de skin para a próxima rotação: {prediction}')

bot.run('token_do_bot')
