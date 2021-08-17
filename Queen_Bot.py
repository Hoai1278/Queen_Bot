import discord
import os
from discord.ext import commands,tasks
import asyncio
import random
import math
import datetime
import time

#########################
###########||############
#######\\##||##//########
########\\####//#########
#####____#######____#####
########//####\\#########
#######//##||##\\########
###########||############
#########################

client = commands.Bot(command_prefix = "Mi ")

@client.event
async def on_ready():
    global ConsoleChannel
    ConsoleChannel = client.get_channel(856882963107282967)
    await ConsoleChannel.send("{0.user} ready to serve the kingdom.".format(client))
    global DMChannel
    DMChannel = client.get_channel(875548856471928873)

@client.event
async def on_message(message):
  global mention
  mention = f'<@!{client.user.id}>'
  if message.author == client.user:
    return
  if message.content.startswith(message.content) and message.author.id != 854008226697314384 and message.author.id != 872515047841226752:
      if message.channel.type == discord.ChannelType.private:
            DM = str(message.author.name+str(message.author.id)+" wrote DM "+  "'"+message.content+"'")
            await DMChannel.send(DM)

  await client.process_commands(message)

@client.command()
async def send(ctx,channelID : int,txt):
  SendChannel = client.get_channel(channelID)
  await SendChannel.send(txt)

@client.command()
async def DM(ctx,user : discord.User,txt):
  await user.send(txt)

@client.event
async def on_command_error(ctx,error):
    await ctx.send(error)

@client.command()
async def time(ctx):
    local_time = datetime.datetime.now()
    current = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.send("Year:"+str(local_time.year)+"\n Month-date:"+str(local_time.month)+":"+str(local_time.day)+"\n Time:"+str(current))

@client.command()
async def print(ctx,*,txt):
    await ctx.send(txt)

@client.command()
async def quote(ctx,txt,ID : discord.Member=None):
    if ID == None:
        await ctx.send('"'+txt+'"' '\n' '\n       -{0}, {1}'.format(ctx.author,datetime.datetime.now().year))
    else:
        await ctx.send('"'+txt+'"' '\n' '\n       -{0}, {1}'.format(ID,datetime.datetime.now().year))

@client.command()
async def ask(ctx,*,question):
    fixedYesAns = ["Is Francesc bad?"]
    fixedNoAns = ["Is Francesc good?"]
    if "?" in question:
        if question in fixedYesAns:
            await ctx.reply("Yes!")
        elif question in fixedNoAns:
            await ctx.reply("No!")
        else:
            ans = ["Yes!","No!","Not sure","Probably","Probably not"]
            await ctx.reply(random.choice(ans))
    else:
        await ctx.reply("question must have \"?\"")
@client.command()
async def kill(ctx,*,user : discord.Member):
    response = ["{0} stabbed {1} to death.","{0} drowned {1} to death.","{0} shot {1} in the head.","{0} fucked {1} to death.","{1} died from laughing to death","{1} masturbated to death","{1} fell down from the bed to death","{0} pushed {1} from a building to death","{1} died from drugs overused",
                "{0} roasted {1} to death."]
    pick = random.choice(response)
    if ctx.author != user:
        if user != "<@!364352649883025408>":
            await ctx.send(pick.format(ctx.author.mention,user.mention))
        else:
            await ctx.send("You can't kill the king, dumbass!")
    elif ctx.author == user:
        await ctx.send(" {} comitted suicide".format(ctx.author.mention))

@client.command()
async def suicide(ctx):
    await ctx.send(" {} comitted suicide".format(ctx.author.mention))

@client.command(aliases = ["b"])
async def ban(ctx,user : discord.Member,*,reason=None):
    if ctx.author.guild_permissions.administrator == True:
        await user.ban(reason=reason)
        await user.send("You have been banned from server {} for" + reason.format(ctx.guild.name))
        await ctx.send("{} has been banned from this server for {}".format(user.mention, reason))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["ub"])
async def unban(ctx,user : discord.Member):
    if ctx.author.guild_permissions.administrator == True:
        bannedUsers = await ctx.guild.bans()
        memberName, memberDiscrimator = user.split("#")
        for banEntry in bannedUsers:
            users = banEntry.user
            if (user.name, user.discriminator) == (memberName, memberDiscrimator):
                await ctx.guild.unbans(user)
                await user.send("You have been unbanned from server {}.".format(ctx.guild.name))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["k"])
async def kick(ctx,user : discord.Member,*,reason=None):
    if ctx.author.guild_permissions.administrator == True:
        await user.kick(reason=reason)
        await user.send("You have been kicked from server {} for" + reason.format(ctx.guild.name))
        await ctx.send("{} has been kicked from this server for {}".format(user.mention, reason))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["m"])
async def mute(ctx,user : discord.Member,*,reason=None):
    if ctx.author.guild_permissions.administrator == True:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await user.add_roles(mutedRole, reason=reason)
        await ctx.send("{} have been muted for {}".format(user.mention, reason))
        await user.send("You have been muted in server {}".format(ctx.guild.name))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["um"])
async def unmute(ctx,user : discord.Member):
    if ctx.author.guild_permissions.administrator == True:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(mutedRole)
        await ctx.send("{} have been unmuted".format(user.mention))
        await user.send("You have been unmute in server {}".format(ctx.guild.name))
    else:
        await ctx.send("You're not the Administrator!")
def main():
    TOKEN1 = "ODc1NDA1ODU3NDE0ODY0ODk2.YRVDPA.7MrFbQgqLD7iZBLqCyotO_k1Ehc"
    client.run(TOKEN1)