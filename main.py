from discord.ext import commands
import discord
import asyncio
bot = commands.Bot(command_prefix='!', self_bot=True)
token = input("Enter your token: ")
@bot.command()
async def massdm(ctx, delay:int=0, *, message:str):
    for member in ctx.guild.members:
        try:
            await member.send(message)
            await asyncio.sleep(delay)
        except Exception as e:
            print(e)
bot.run(token)            