<<<<<<< HEAD
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

joke_list = ["I'VE GOT A JOKE,", "JOKE,", "IK WEET EEN MOP,", "IK KEN EEN MOP,", "IK KEN EEN GRAP,", "GRAP," ]
bypass_list = []
pain_scale = [" Subject suffered a broken nose.", " Subject rendered unconscious.", " Subject killed."," Subject injured, two teeth dislodged.", " Subject severely injured, right eye destroyed by piece of tomato.", " Chipped tooth and hairline jaw fracture.", " Subject is hospitalized with a massive skull fracture."]

@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    x = random.randint(1,1000)
    contents = message.content.split(" ")
    #msg = message.content.split(" ", 1)
    for word in contents:
        if word.upper() in joke_list:
            if not message.author.id in bypass_list:   
                 await client.send_message(message.channel,"```Item: One mature SCP-504 tomato \n" + "Subject: D-504-1 \n" +"Spoken: "+ "[REDACTED]" +"\n" + "Tomato clocked at " + str(x)  +" mph." + random.choice(pain_scale) +"```" )

  # message.content = message.content.lower()
    #if message.content in joke_list:
    #if joke_list in message.content.lower():
       

client.run('TOKEN')
#Item: One mature SCP-504 tomato
#Subject: D-504-1
#Spoken: "insert what came after the joke prefix"
#Result: Tomato clocked at "insert random number here" mph. "insert damage here".
=======
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

joke_list = ["I'VE GOT A JOKE,", "JOKE,", "IK WEET EEN MOP,", "IK KEN EEN MOP,", "IK KEN EEN GRAP,", "GRAP," ]
bypass_list = []
pain_scale = [" Subject suffered a broken nose.", " Subject rendered unconscious.", " Subject killed."," Subject injured, two teeth dislodged.", " Subject severely injured, right eye destroyed by piece of tomato.", " Chipped tooth and hairline jaw fracture.", " Subject is hospitalized with a massive skull fracture."]

@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    x = random.randint(1,1000)
    contents = message.content.split(" ")
    #msg = message.content.split(" ", 1)
    for word in contents:
        if word.upper() in joke_list:
            if not message.author.id in bypass_list:   
                 await client.send_message(message.channel,"```Item: One mature SCP-504 tomato \n" + "Subject: D-504-1 \n" +"Spoken: "+ "[REDACTED]" +"\n" + "Tomato clocked at " + str(x)  +" mph." + random.choice(pain_scale) +"```" )

  # message.content = message.content.lower()
    #if message.content in joke_list:
    #if joke_list in message.content.lower():
       

client.login('TOKEN')
#Item: One mature SCP-504 tomato
#Subject: D-504-1
#Spoken: "insert what came after the joke prefix"
#Result: Tomato clocked at "insert random number here" mph. "insert damage here".
>>>>>>> 22ceb86531d1f3264a76852a53712450a6404ed5
