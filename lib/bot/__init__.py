#Imports
import discord
from discord.ext import commands
import os

#Cogs List
cogs = []
for i in os.listdir("lib/cogs"):
    if i.endswith(".py"):
        cogs.append(i[:-3])



#Create Class Bot
class Bot(commands.Bot):

    #Init Function
    def __init__(self, prefix, ownersId):
        self.prefix = prefix
        self.ownersId = ownersId
        self.ready = False
        self.guild = None
        super().__init__(command_prefix = self.prefix, owner_ids = self.ownersId, intents = discord.Intents.all())
        self.remove_command("help")

        #Colors For The Console Logs
        self.colors = {
            "yellow": "\033[93m",
            "red": "\033[91m",
            "green": "\033[1;32;40m",
            "blue": "\033[94m",
            "cyan": "\033[96m",
            "purple": "\033[95m",
            "white": "\033[0m"
        }

    
    #Cogs Setup Function
    def cogSetup(self):
        for cog in cogs:
            self.load_extension(f"lib.cogs.{cog}")


    #Bot Run Function
    def run(self, version):
        self.version = version
        with open("lib/bot/token", "r") as file:
            self.token = file.read()
        
        self.cogSetup()

        print("Starting Bot")
        super().run(self.token, reconnect=True)


    #On Bot Connect Event
    async def on_connect(self):
        print(f"{self.user} is connected")

    #On Bot Disconnect Event
    async def on_disconnect(self):
        print(f"{self.user} is disconnected")

    #On Bot Ready Event
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print(f"{self.user} is ready to rumble!")
            self.owner = self.get_user(self.ownersId[0])
            #Change The Default Activity Of The Bot
            self.defaultActivity = discord.Game(name="|Write !help|")
            await self.change_presence(activity=self.defaultActivity)

        else:
            print(f"{self.user} reconnected")


    #On Bot Joins Server Event
    async def on_guild_join(self, guild):
        print(self.colors["yellow"]+f"{self.user} has joined {guild}"+self.colors["white"])

    #On Bot Leaves Server Event
    async def on_guild_remove(self, guild):
        print(self.colors["yellow"]+f"{self.user} has left {guild}"+self.colors["white"])


    #On Member Joins Server Event
    async def on_member_join(self, member):
        print(self.colors["yellow"]+f"{member} has joined {member.guild}"+self.colors["white"])

    #On Member Leaves Server Event
    async def on_member_remove(self, member):
        print(self.colors["yellow"]+f"{member} has left {member.guild}"+self.colors["white"])


    #On General Error Event
    async def on_error(self, error, *args, **kwargs):
        raise

    #On General Command Error Event
    async def on_command_error(self, ctx, error):
        if type(error) == commands.CommandNotFound:
            print(self.colors["red"]+f"{ctx.message.author} wrote a non existing command in {ctx.message.guild} server\nMessage: \"{ctx.message.content}\""+self.colors["white"])
        else:
            print(self.colors["red"]+f"{ctx.message.author} got the error \"{error}\" saying \"{ctx.message.content}\" in {ctx.message.guild} server"+self.colors["white"])