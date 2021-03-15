#Imports
import discord
from discord.ext import commands
from random import randint
import os



#Create Class Commands Cog
class Commands(commands.Cog):

    #Init Function
    def __init__(self, bot):
        self.bot = bot
        self.ready = False
    
    #On Bot Ready Event
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.ready:
            print(self.bot.colors["green"]+"Commands Cog Ready"+self.bot.colors["white"])
        else:
            print(self.bot.colors["green"]+"Commands Cog Reconnected"+self.bot.colors["white"])



    #Command Ping
    @commands.command(name="ping")
    async def ping(self, ctx):
        if ctx.guild != None:
            print(self.bot.colors["blue"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])
            await ctx.send("pong")
            #Send A File
            # await ctx.send(file=discord.File("data\\img\\image.png"))



#Adds The Cog To The Bot
def setup(bot):
    bot.add_cog(Commands(bot))