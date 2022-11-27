import os
import discord
from discord.ext import commands
import asyncio

TOKEN = os.getenv('DISCORD_TOKEN', "MTA0NjUxNDIyNjcxOTY0MTYyMQ.GZ193h.FU_Gf2-e8phESRkLKqepq3xc3px5mBSKcDFWXc")

intents = discord.Intents.default()
intents.members = True

# client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='!', intents=intents)


# @commands.Cog.listener()
# async def on_ready(self):
#     print(f'{bot.user} has connected to Discord!')
#     guild = bot.guilds[0]
#     members = "\n -".join([memb.name for memb in guild.members])
#     print(f"Guild Members:\n{members}")

async def main():
    async with bot:
        await bot.load_extension("cogs.Greetings")
        await bot.start(TOKEN)


asyncio.run(main())
