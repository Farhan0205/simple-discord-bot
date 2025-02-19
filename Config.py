#General Mod Config
[general]
	#The Token of the Bot to use. KEEP THIS PRIVATE
	botToken = ""
	#Should the bot be enabled or not
	enabled = true
	#Should debug logging be enabled? WARNING: THIS CAN SPAM YOUR LOG!
	debugging = false
	#How quickly the bot status should update
	activityUpdateInterval = 30
	#The prefix to use for bot commands. Example: ~players
	botPrefix = "~"
	#Should the bot be allowed to whitelist/un-whitelist players. Whitelisting needs to be enabled on your server as well
	whitelisting = true
	#Should only admins be allowed to whitelist players
	onlyAdminsWhitelist = false
	#Do not add Playing. A status to display on the bot. You can use %players% and %maxplayers% to show the number of players on the server
	botStatus = "Minecraft"
	#A topic for the Chat Relay channel. You can use %player%, %maxplayers%, %uptime%, %tps% or just leave it empty.
	channelTopic = "Playing Minecraft with %players%/%maxplayers% people | Uptime: %uptime%"
	#Discord Invite Link used by the in-game invite command
	inviteLink = ""
	#Internal version control. DO NOT TOUCH!
	configVersion = 10

#Webhook Config
[webhookConfig]
	#Should webhook messages be used
	enabled = true
	#The URL of the channel webhook to use for Chat Messages
	webhookurl = "https://discord.com/api/webhooks/1059502731510943785/VxuInhPQxgCnq7WQZkBOYF2hLYF_EsmQYxj5u_3Z7FTvSsvgjT4Ce9BYgrA7UWvyEUv7"
	#The URL of the channel webhook to use for Server Messages Messages
	webhookurlLogs = "https://discord.com/api/webhooks/1059502731510943785/VxuInhPQxgCnq7WQZkBOYF2hLYF_EsmQYxj5u_3Z7FTvSsvgjT4Ce9BYgrA7UWvyEUv7"
	#A DIRECT link to an image to use as the avatar for server messages. Also used for embeds
	serverAvatar = ""
	#The name to display for Server messages when using Webhooks
	serverName = "Minecraft Server"

#Chat Config
[chatConfig]
	#The ID of the channel to post in and relay messages from. This is still needed, even in webhook mode
	channelID = 0
	#If this ID is set, event messages will be posted in this channel instead of the chat channel
	logChannelID = 0
	#The type of image to use as the player icon in messages. Valid entries are: AVATAR, HEAD, BODY, COMBO
	playerAvatarType = "COMBO"
	#Should embeds be used instead of plain text messages for Chat Messages
	useEmbeds = true
	#Should embeds be used instead of plain text messages for Log Messages
	useEmbedsLog = true
	#Prefix to add to Minecraft when a message is relayed from Discord. Supports MC formatting. Use %user% for the Discord Username
	mcPrefix = "§e[Discord]§r %user%: "
	#Should messages from bots be relayed
	ignoreBots = true
	#Should SERVER STARTING messages be shown
	serverStarting = true
	#Should SERVER STARTED messages be shown
	serverStarted = true
	#Should SERVER STOPPING messages be shown
	serverStopping = true
	#Should SERVER STOPPED messages be shown
	serverStopped = true
	#Should the chat be relayed
	playerMessages = true
	#Should Join and Leave messages be posted
	joinAndLeaveMessages = true
	#Should Advancement messages be posted
	advancementMessages = true
	#Should Death Announcements be posted
	deathMessages = true
	#Should Messages from the /say command be posted
	sendSayCommand = true
	#Should commands be posted to discord
	broadcastCommands = true
	#Should Tell Raw messages be posted
	sendTellRaw = true
	#Should the ~discord command be enabled
	inviteCommandEnabled = false

#Change the contents of certain event messages
[messages]
	#Server Starting Message
	serverStarting = "Server is starting..."
	#Server Started Message
	serverStarted = "Server has started. Enjoy!"
	#Server Stopping Message
	serverStopping = "Server is stopping..."
	#Server Stopped Message
	serverStopped = "Server has stopped..."
	#Player Joined Message. Use %player% to display the player name
	playerJoined = "%player% has joined the server!"
	#Player Left Message. Use %player% to display the player name
	playerLeft = "%player% has left the server!"
	#Achievement Messages. Available variables: %player%, %title%, %description%
	achievements = "%player% has made the advancement [%title%]: %description%"
	#Chat Messages. Available variables: %player%, %message%
	chat = "%message%"
	#The message to show when someone uses /discord command. You can use %inviteurl%
	inviteMessage = "Hey, check out our discord server here -> %inviteurl%"

#Change in which channel messages appear
[messageDestinations]
	#Should Server Starting/Started/Stopping/Stopped Messages be in chat. If false, it will appear in the log channel
	statusInChat = false
	#Should Join/Leave Messages be in chat. If false, it will appear in the log channel
	joinLeaveInChat = false
	#Should Advancement Messages be in chat. If false, it will appear in the log channel
	advancementsInChat = false
	#Should Death messages be in chat. If false, it will appear in the log channel
	deathInChat = false
