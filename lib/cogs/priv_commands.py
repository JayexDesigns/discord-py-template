#Imports
import discord
from discord.ext import commands



#Create Class Private Commands Cog
class PrivateCommands(commands.Cog):

    #Init Function
    def __init__(self, bot):
        self.bot = bot
        self.ready = False
    
    #On Bot Ready Event
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.ready:
            print(self.bot.colors["green"]+"Private Commands Cog Ready"+self.bot.colors["white"])
        else:
            print(self.bot.colors["green"]+"Private Commands Cog Reconnected"+self.bot.colors["white"])



    #Get Bot Server List
    @commands.command(name="server_list")
    async def server_list(self, ctx):
        if ctx.author == self.bot.owner:
            print(self.bot.colors["cyan"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])
            serverEmbed = discord.Embed(title="Server List", colour=ctx.author.color)

            for i in self.bot.guilds:
                serverEmbed.add_field(name=i.name, value=f":green_circle: {len(list(filter(lambda m: str(m.status) == 'online', i.members)))}", inline=False)

            await ctx.send(embed=serverEmbed)


    #Get Server Information
    @commands.command(name="server_info")
    async def server_info(self, ctx, *, server = None):
        if (ctx.guild == None and ctx.author == self.bot.owner) or ctx.guild != None:
            print(self.bot.colors["cyan"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])
            if server == None:
                server = str(ctx.guild)
                if server == "None":
                    await ctx.send(f"{ctx.author.mention} Write the name of the server or write this command in the server you want to obtain info from")
                    return
            for i in range(len(self.bot.guilds)):
                if self.bot.guilds[i].name == server:
                    guild = self.bot.guilds[i]

                    statuses = [
                        len(list(filter(lambda m: str(m.status) == "online", guild.members))),
                        len(list(filter(lambda m: str(m.status) == "idle", guild.members))),
                        len(list(filter(lambda m: str(m.status) == "dnd", guild.members))),
                        len(list(filter(lambda m: str(m.status) == "offline", guild.members)))
                    ]

                    serverEmbed = discord.Embed(title=guild.name, description="Server Info", colour=ctx.author.color)

                    serverFields = [
                        ("ID", guild.id, False),
                        ("Owner", guild.owner, True),
                        ("Region", guild.region, True),
                        ("Created", guild.created_at.strftime("%d/%m/%Y"), True),
                        ("Users", guild.member_count, True),
                        ("Bots", len(list(filter(lambda m: m.bot, guild.members))), True),
                        ("Status", f":green_circle: {statuses[0]} :orange_circle: {statuses[1]} :red_circle: {statuses[2]} :white_circle: {statuses[3]}", True),
                        ("Text Channels", len(guild.text_channels), True),
                        ("Voice Channels", len(guild.voice_channels), True),
                        ("Categories", len(guild.categories), True),
                        ("Roles", len(guild.roles), True)
                    ]

                    for name, value, inline in serverFields:
                        serverEmbed.add_field(name=name, value=value, inline=inline)
                    serverEmbed.set_thumbnail(url=guild.icon_url)

                    await ctx.send(embed=serverEmbed)
                    return
            else:
                await ctx.send(f"{ctx.author.mention} I don't have information about the server: \"{server}\"")


    #Get User Information
    @commands.command(name="user_info")
    async def user_info(self, ctx, *, memberId = None):
        if ctx.guild != None:
            print(self.bot.colors["cyan"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])

            if memberId == None:
                member = ctx.author

            else:
                try:
                    memberId = int(memberId)
                    member = ctx.guild.get_member(memberId)
                    if member == None:
                        for i in self.bot.guilds:
                            member = i.get_member(memberId)
                            if member != None:
                                break
                        else:
                            await ctx.send(f"{ctx.author.mention} I couldn't find the user")
                            return

                except:
                    try:
                        memberId = memberId[2:len(memberId)-1]
                        if memberId[0] == "!":
                            memberId = memberId[1:]
                        member = ctx.guild.get_member(int(memberId))
                        if member == None:
                            for i in self.bot.guilds:
                                member = i.get_member(int(memberId))
                                if member != None:
                                    break
                            else:
                                await ctx.send(f"{ctx.author.mention} I couldn't find the user")
                                return

                    except:
                        await ctx.send(f"{ctx.author.mention} \"{memberId}\" Is not a valid ID")
                        return

            
            if member.status != member.desktop_status:
                status = "Online Móvil"
            else:
                if str(member.status) == "dnd":
                    status = "Occupied"
                elif str(member.status) == "idle":
                    status = "IDLE"
                else:
                    status = str(member.status).title()

            
            userEmbed = discord.Embed(title=member.name, description="User Info", colour=member.color)

            userFields = [
                ("ID", member.id, False),
                ("Bot", "Yes" if member.bot else "No", True),
                ("Rol", member.top_role, True),
                ("Status", status, True),
                ("Activty", member.activity.name if member.activity else "N/A", True),
                ("Created", member.created_at.strftime("%d/%m/%Y"), True),
                ("Nitro", member.premium_since.strftime("%d/%m/%Y") if member.premium_since != None else "No Nitro", True)
            ]

            for name, value, inline in userFields:
                userEmbed.add_field(name=name, value=value, inline=inline)

            userEmbed.set_thumbnail(url=member.avatar_url)

            await ctx.send(embed=userEmbed)


    #Get Bot DM's
    @commands.command(name="dm_list")
    async def dm_list(self, ctx):
        if ctx.author == self.bot.owner:
            print(self.bot.colors["cyan"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])
            dmEmbed = discord.Embed(title="Direct Messages", colour=ctx.author.color)
            for i in self.bot.private_channels:
                dmEmbed.add_field(name=i.recipient.name, value=str(i.type).title(), inline=False)
            await ctx.send(embed=dmEmbed)
        else:
            print(self.bot.colors["red"]+f"{ctx.message.author} tried to see the bot's dm list in {ctx.message.guild} server"+self.bot.colors["white"])
            await ctx.send(f"{ctx.author.mention} You can't use this command")



    #Clear Messages Command
    @commands.command(name="message_clear")
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def message_clear(self, ctx, amount=1):
        if ctx.guild != None:
            print(self.bot.colors["cyan"]+f"{ctx.message.author} says {ctx.message.content} in {ctx.message.guild} server"+self.bot.colors["white"])
            await ctx.channel.purge(limit=amount+1)

    #Error When Using Message Clear
    @message_clear.error
    async def message_clear_error(self, ctx, error):
        if type(error) == commands.errors.BotMissingPermissions:
            await ctx.send(f"{ctx.author.mention} I can't delete messages because I'm not allowed to")



#Adds The Cog To The Bot
def setup(bot):
    bot.add_cog(PrivateCommands(bot))