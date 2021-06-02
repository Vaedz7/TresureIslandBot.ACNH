'''EDIT THE FOLLOWING LINES'''
token="Token" #If no token set bot will not start
prefix="$" #Default $
status="None" #If set to None status will be Playing a Game: Animal Crossing: New Horizons
role_name="TreasureIslandBot.ACNH" #If set to None role will be called None. Default TreasureIslandBot.ACNH
user_limit="None" #Set None for unlimited users. If set to None Dodo will not be private
support_server_inv="None" #If set to none then help command will say "DM my owner for help"
island_name="Island" #It will show in info command so users can double check they are going to the correct place.
owner_name="Owner" #It will show in info command so users can check owner. It may also show in help command.
add_keepalive=False #If set to False the bot will stop every ~30 min. If true you will need to complete extra steps in the wiki but bot will stay online.
'''DO NOT EDIT THE FOLLOWING'''



#----------------------------------------------------------------



import json
import discord
import os
import sys
from discord.ext import commands
import keep_alive

client = commands.Bot(command_prefix=[prefix])
client.remove_command('help')

def pather(guild_id, channel_id, filename, default_value):
    path = sys.path[0] + '/' + str(guild_id) + '/' + str(channel_id) + '/'

    if not os.path.exists(str(guild_id) + '/' + str(channel_id)):
        os.makedirs(str(guild_id) + '/' + str(channel_id))

    if not os.path.isfile(path + filename):
        with open(path + filename, 'w+') as file:
            file.write(str(default_value))

    return path


@client.event
async def on_ready():
    global status
    print("Island Online on {} | ID {}".format(client.user.name, client.user.id))
    if status == "None":
      await client.change_presence(activity=discord.Game("Animal Crossing: New Horizons!"))
    else:
      await client.change_presence(activity=discord.Game(status))


@client.command()
async def ping(ctx): """Gets the latency of the bot in ms"""; await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

members=0

@client.command()
async def join(ctx):
  global user_limit
  global members
  if user_limit == "None" or int(user_limit)>int(members):
    global role_name
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    user = ctx.message.author
    await user.add_roles(role)
    members=members+1
    x=str(ctx.message.author.mention)+" has joined the island.\nWhen you are leaving please use the ``leave`` command.\nCurrent visitor count: "+str(members)+"."
    await ctx.send(x)
  else:
    await ctx.send("Sorry the max number of users has been reached. Please wait for someone to use ``leave`` command")

@client.command()
@commands.has_any_role(role_name)
async def leave(ctx):
    global members
    global role_name
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    user = ctx.message.author
    await user.remove_roles(role)
    members=members-1
    x=str(ctx.message.author.mention)+" has left the island.\nEnjoy your items\nCurrent visitor count: "+str(members)+"."
    await ctx.send(x)

dodo="00000"

@client.command()
async def code(ctx):
  global user_limit
  global dodo
  global members
  if user_limit == "None":
    global dodo
    x="Dodo Code: "+dodo+"."
    await ctx.send(x)
  else:
    if int(user_limit) > int(members):
      x="Dodo Code: "+dodo+"."
      y=ctx.message.author.mention+" I sent you the Dodo Code via DM. If you did not recieve it you may have your DMs blocked."
      await ctx.send(y)
      return await ctx.message.author.send(x)
    else:
      await ctx.send("Sorry the max number of users has been reached. Please wait for someone to use ``leave`` command")

@client.command()
@commands.is_owner()
async def setcode(ctx, arg):
  global dodo
  dodo=arg
  x="The dodo code for the bot has been set to "+dodo+"."
  await ctx.send(x)

@client.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
  global role_name
  guild = ctx.guild
  await guild.create_role(name=role_name)
  x=role_name+" role created."
  await ctx.send(x)

@client.command()
async def help(ctx):
  global support_server_inv
  if support_server_inv == "None":
    await ctx.send("DM "+owner_name+" for help.")
  else:
    x="Join the support server: "+support_server_inv
    await ctx.send(x)

@client.command()
async def info(ctx):
  emb="**Info**\n**Owner:** "+owner_name+"\n**Version:** 1.1.0\n**Island:** "+island_name+"\n**Servers:** "+str(len(client.guilds))
  embed=discord.Embed(title="I am a Discord Bot powered by Vaedz TreasureIslandBot.ACNH software", description=emb)
  await ctx.send("Here's a bit about me!")
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def reset(ctx):
  global members
  members=0
  await ctx.send("Reset Island Visitors")

if add_keepalive == True:
  keep_alive.keep_alive

client.run(token)
