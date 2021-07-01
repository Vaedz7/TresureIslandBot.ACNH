# **Important**
Coming Soon - Optional CFW on Switch to run switch based features

# **HOME**
Welcome to the TreasureIslandBot.ACNH wiki!

This Wiki will cover how to set up and use TreasureIslandBot.ACNH

# **Customization Options Discord**
Here are fields of your bot that you can customize!

**Required Custom Fields - These are required to start the bot**

- **Token:** This is your bot token that can be found in your bots developer portal page

**Important Custom Fields - These are required to have the bot run at its full potential**

- **Island Name:** This is the name of your Island. It is used in the info command.

- **Owner Name:** This is your discord name and tag (EX. Bothost#1234) it is used in the info command and sometimes in the help command.

**Crucial Custom Fields - These will affect how the bot functions but won't deteriorate the functions either way**

- **User Limit:** This is to limit the number of users that can be on your Island at once. If set to none then the bot will show Dodo code publicly in requested channel rather than DMs. if set to any number the bot will DM the code when requested but will not DM the code if max limit has been reached.

- **Add Keep Alive:** This will toggle the "keep_alive" function. If set to False the bot will go offline every ~30 minuets of inactivity. If set to True the bot will stay alive until stopped. To set this to True you will need to complete Step 4 of Computer/Discord setup. if you have this set as False ignore step 4.

- **Support Server Inv:** Adding a support server invite will direct users that use the help command to the support server. If you leave this as None the owner name will be used in the help command and the user will be directed to DM you.

**Changeable Custom Fields - These will change aspects of the bot but the bot can run properly no matter how you use these fields**

- **Prefix:** This is to change the bots prefix (Default: $)

- **Status:** This is to change the bots status (Default: Animal Crossing: New Horizons!)

- **Role Name:** This is to change the role that the bot uses to manage the Island (Default: TreasureIslandBot.ACNH)

# **Customization Options Twitch**
Here are fields of your bot that you can customize!

**Required Custom Fields - These are required to start the bot**

- **OAuth Token:** This is your Twitch Account OAuth Token. If you need help finding this view this guide https://twitchapps.com/tmi/.

- **Client ID:** This is your Developer Client ID. If you need help finding this view this guide https://dev.twitch.tv/login.

- **Bot Channel:** This is the stream/channel that the bot will operate in.

- **Bot Nickname:** This is to verify the bot if this is incorrect then the bot won't run.

**Important Custom Fields - These are required to have the bot run at its full potential**

- **Dodo Code:** This is the Island DODO Code. If not inputted correctly users will not be able to join your island.

- **Island Name:** This is the name of your Island. It is used in the info command.

- **Owner Name:** This is your twitch username (EX. Bothost) it is used in the info command and sometimes in the help command.

**Crucial Custom Fields - These will affect how the bot functions but won't deteriorate the functions either way**

- **User Limit:** This is to limit the number of users that can be on your Island at once. If set to none then the bot will show Dodo code publicly in stream chat rather than Whisper. If set to any number the bot will Whisper the code when requested but will not Whisper the code if max limit has been reached.

- **Add Keep Alive:** This will toggle the "keep_alive" function. If set to False the bot will go offline every ~30 minuets of inactivity. If set to True the bot will stay alive until stopped. To set this to True you will need to complete Step 4 of Twitch/Stream setup. if you have this set as False ignore step 4.

- **Support Server Inv:** Adding a support server invite will direct users that use the help command to the support server. If you leave this as None the owner name will be used in the help command and the user will be directed to Whisper you.

**Changeable Custom Fields - These will change aspects of the bot but the bot can run properly no matter how you use these fields**

- **Prefix:** This is to change the bots prefix (Default: $)

# **Requirements**
Here is what you will need to set up your own bot.

- **Nintendo Switch (Does not need CFW)** - $299

- **Animal Crossing: New Horizons** - $59.99

- **Nintendo Switch Online** - $19.99 Yearly OR $3.99 Monthly

For Discord Bot:

- **Discord Account and Server** - Free

For Twitch Bot:

- **Twitch Accounts OAuth Token and Client ID (See Setup)** - Free

# **Discord Bot Setup**
Ready to set up your own bot? Make sure you have everything from Requirements before you continue.

**Step 1:** Make a Bot using https://discord.com/developers/applications.

**Step 2:** Download the code from this Repo.

**Step 3:** In the main.py file edit all custom fields to preference. If you mark keep alive as False then skip to step 5.

**Step 4:** Read this guide - https://replit.com/talk/learn/Hosting-discordpy-bots-with-replit/11008.

**Step 5:** Invite your bot by getting an OAuth2 link.

**Step 6:** Run your bot!

# **ACNH Setup for Discord**
Once you have your Computer/Discord setup done you can move on to the ACNH setup.

**Step 1:** Have your treasure island ready to go. You can get the items you wanna give away using an ACNH Sysbot. If many people are using your Island then you should try and have a refresh time where your Island is being restocked and not open to visitors.

**Step 2:** When the bot is online make sure the switch is also online. You can do this by using an Arduino that will automate a joystick press every 1 minute to reset the power off counter.

**Step 3:** Read Customization Options for details to help members and to limit activity.

# **Twitch Bot Setup**
Ready to set up your own bot? Make sure you have everything from Requirements before you continue.

**Step 1:** Make a new Twitch account for your bot.

**Step 1.5:** Make sure your new account has a OAuth Token - https://twitchapps.com/tmi/ and a Client ID - https://dev.twitch.tv/login

**Step 2:** Download the code from this Repo.

**Step 3:** In the twitch.py file edit all custom fields to preference. If you mark keep alive as False then skip to step 5.

**Step 4:** Read this guide - https://replit.com/talk/learn/Hosting-discordpy-bots-with-replit/11008. Complete the same steps as the guide says because Twitch and Discord use the same keep_alive function. 

**Step 6:** Run your bot! It should run on the set channel!

# **ACNH Setup for Twitch**
Once you have your Twitch/Stream setup done you can move on to the ACNH setup.

**Step 1:** Have your treasure island ready to go. You can get the items you wanna give away using an ACNH Sysbot. If many people are using your Island then you should try and have a refresh time where your Island is being restocked and not open to visitors.

**Step 2:** When the stream and bot are online make sure the switch is also online. You can do this by using an Arduino that will automate a joystick press every 1 minute to reset the power off counter. If you want to stream the switch's screen feel free to do so as it will not affect the bots performance.

**Step 3:** Read Customization Options for details to help members. Limiting activity is now available for Twitch as well and can be viewed in Customization Options

# **TreasureIslandBot.ACNH File Directory**
**Latest Release:**

- discord.py

- twitch.py

- README.md

**Older Releases:**

- discord 1.0.0.py

- twitch 1.0.0.py

- README 1.0.0.md

*keep_alive.py will not update with most releases*

**Thanks for Reading!**
-----------------------
