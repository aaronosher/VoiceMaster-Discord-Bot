import discord
from discord.ext import commands
import traceback
import sys

bot = commands.Bot(command_prefix="vm!")

bot.remove_command("help")

DISCORD_TOKEN = 'NzU5NDk2NzE3ODU0MTc5MzM4.X2-WcA.H7RJRbh7RGgc6smef005G3BC2QI'

initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(DISCORD_TOKEN)
