import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="?")

joke_list = ["JOKE,", "MOP,", "GRAP,"]
bypass_list = []
pain_scale = [" Subject suffered a broken nose.", " Subject rendered unconscious.", " Subject killed.", " Subject injured, two teeth dislodged.",
              " Subject severely injured, right eye destroyed by piece of tomato.", " Chipped tooth and hairline jaw fracture.", " Subject is hospitalized with a massive skull fracture."]


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.event
async def on_message(message):
    if message.author == Client.user:
        return
    if message.author.bot:
        return
    x = random.randint(1, 767)
    contents = message.content.split(" ")
    msg = message.content.split(" ", 1)
    response = ("```Item: One mature SCP-504 tomato \n" + "Subject: D-504-1 \n" + "Spoken: " +
                str(msg) + "\n" + "Tomato clocked at " + str(x) + " mph." + random.choice(pain_scale) + "```")

    for word in contents:
        if word.upper() in joke_list:
            if not message.author.id in bypass_list:
                 await bot.send_message(message.channel, str(response))
            else:
                print("shit's in bypass list boi.")
        else:
           # print("Image file detected")
            if message.attachments:
                await bot.send_message(message.channel, str(response))

bot.run('TOKEN')
# "[REDACTED]"
