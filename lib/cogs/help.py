#Imports
import discord
from discord.ext import commands



#Create Class Help Cog
class Help(commands.Cog):

    #Init Function
    def __init__(self, bot):
        self.bot = bot
        self.ready = False
    
    #On Bot Ready Event
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.ready:
            print(self.bot.colors["green"]+"Help Cog Ready"+self.bot.colors["white"])
        else:
            print(self.bot.colors["green"]+"Help Cog Reconnected"+self.bot.colors["white"])



    #Command Help
    @commands.command(name="help")
    async def help(self, ctx):
        if ctx.guild != None:
            print(self.bot.colors["blue"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])
            commandsEmbed = discord.Embed(title="Commands:", colour=0xFF0066)
            privCommandsEmbed = discord.Embed(title="Information Commands:", colour=0x00CCFF)
            infoEmbed = discord.Embed(title="Information:", colour=0x00FFA6)

            commandsFields = [
                ("!ping", "pong", True)
            ]
            privCommandsFields = [
                ("!server_info", "Shows you info from the server you write this", True),
                ("!user_info [user]", "Shows info of the mentioned user", True),
                ("!message_clear [ammount]", "Deletes a specified amount of messages if the bot is allowed to do so", True)
            ]
            infoFields = [
                ("Bot", "This is a bot template made by [Jayex Designs](https://twitter.com/Jayex_Designs)", False)
            ]

            for name, value, inline in commandsFields:
                commandsEmbed.add_field(name=name, value=value, inline=inline)
            
            for name, value, inline in privCommandsFields:
                privCommandsEmbed.add_field(name=name, value=value, inline=inline)

            for name, value, inline in infoFields:
                infoEmbed.add_field(name=name, value=value, inline=inline)
            infoEmbed.set_footer(text=f"v: {self.bot.version}")

            await ctx.send(embed=commandsEmbed)
            await ctx.send(embed=privCommandsEmbed)
            await ctx.send(embed=infoEmbed)



#Adds The Cog To The Bot
def setup(bot):
    bot.add_cog(Help(bot))