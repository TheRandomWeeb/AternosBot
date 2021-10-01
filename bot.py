from discord.ext import commands
from scrapper import TurnOnServer, ServerStatus


bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user} is online! FUNNI TIME!')


@bot.command()
async def start(ctx):
    await ctx.send('Attempting... (If this bot does not type anything in the next 2 minutes try again)')
    TurnOnServer()
    await ctx.send('Turning on Server!')
    text = ServerStatus()
    await ctx.send(f'Server is {text}!')

@bot.command()
async def status(ctx):
    text = ServerStatus()
    await ctx.send(f'Server is {text}!')

bot.run('ODkzMzQwNTgzMzU4MjU5Mjcw.YVaCQA.-32uBErtztFJxbEr9twtHlMVBfw')
