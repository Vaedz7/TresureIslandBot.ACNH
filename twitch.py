'''EDIT THE FOLLOWING LINES'''
bot_token="Token" #If no token set bot will not start. This is your Twitch OAuth
clientID="client id" 
bot_prefix="$" #Default $
dodo="00000" #Enter the Islands Dodo Code. If incorrect users won't be able to join. Refresh the bot when you set a new Dodo.
user_limit="None" #Set None for unlimited users. If set to None Dodo will not be private
support_server_inv="None" #If set to none then help command will say "Whisper my owner for help"
bot_channel="channel" #Name of channel you want this bot to run on.
bot_nickname="Twitch TreasureIslandBot.ACNH" #The name of your bot. Default Twitch TreasureIslandBot.ACNH
island_name="Island" #It will show in info command so users can double check they are going to the correct place.
owner_name="Owner" #It will show in info command so users can check owner. It may also show in help command.
add_keepalive=False #If set to False the bot will stop every ~30 min. If true you will need to complete extra steps in the wiki but bot will stay online.
'''DO NOT EDIT THE FOLLOWING'''



#----------------------------------------------------------------



import os
from twitchio.ext import commands
import keep_alive

client = commands.Bot(
    irc_token=bot_token,
    client_id=clientID,
    nick=bot_nickname,
    prefix=bot_prefix,
    initial_channels=bot_channel)

@client.event
async def event_ready():
  print(f"{os.environ['BOT_NICK']} is online!")
  ws = client._ws  # this is only needed to send messages within event_ready
  await ws.send_privmsg(bot_channel, f"/me has opened up the Island")

@client.event
async def event_message(ctx):
  if ctx.author.name.lower() == bot_nickname.lower():
    return
  await client.handle_commands(ctx)

members=0

@client.command(name='join')
async def join(ctx):
  global members
  if user_limit > members or user_limit == "None":
    members=members+1
    x=str(ctx.message.author.mention)+" has joined the island.\nWhen you are leaving please use the ``leave`` command.\nCurrent visitor count: "+str(members)+"."
    await ctx.send(x)
  else:
    await ctx.send("Sorry the max number of users has been reached. Please wait for someone to use leave command")

@client.command(name='leave')
async def leave(ctx):
  global members
  members=members-1
  x=str(ctx.message.author.mention)+" has left the island.\nEnjoy your items\nCurrent visitor count: "+str(members)+"."
  await ctx.send(x)

@client.command(name='code')
async def code(ctx):
  global dodo
  global user_limit
  if user_limit == "None":
    x="Dodo Code: "+dodo+"."
    await ctx.send(x)
  else:
    if user_limit > members:
      x="/w "+ctx.message.author+" Dodo Code: "+dodo+"."
      await ctx.send(x)
    else:
      await ctx.send("Sorry the max number of users has been reached. Please wait for someone to use the leave command")

@client.command(name='help')
async def help(ctx):
  global support_server_inv
  if support_server_inv == "None":
    await ctx.send("Whisper "+owner_name+" for help.")
  else:
    x="Join the support discord server: "+support_server_inv
    await ctx.send(x)

@client.command(name='info')
async def info(ctx):
  x="**I am a Discord Bot powered by Vaedz TreasureIslandBot.ACNH software**\n\n**Info**\n**Owner:** "+owner_name+"\n**Version:** 1.1.0\n**Island:** "+island_name
  await ctx.send(x)

@client.command(name="reset")
@commands.has_permissions(moderator=True)
async def reset(ctx):
  global members
  members=0
  await ctx.send("Reset Island Visitors")

if add_keepalive == True:
  keep_alive.keep_alive

if __name__ == "__main__":
    client.run()
