# Import Discord pkg
import discord
import random
from discord.ext import commands
import pandas as pd


#client PREFIX
client = commands.Bot(command_prefix='/')


#online checking 
@client.event
async def on_ready():
   general_channel = client.get_channel(774826848370163752)

   await   general_channel.send('TOASTING AROUND')
   
   

#lucas ping cmd
@client.command(name="ping")
async def ping(context):
 await context.send('```COMING SOON```')



@client.command(name="8ball")
async def _8ball(ctx):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.", 'do i look like a frikking fortune teller', 'do u think the future is elastic or fixed because if its elastic i cant help u',
    'does this look like a charity service pay me first']
    response = random.choice(responses)
    ball = discord.Embed(title = "Your answer is: ", description = (response), color = 0x133337)     
    await ctx.message.channel.send(embed = ball)

client.run('NzA0MDM3OTI1OTA1NDk4MTY0.XqXUaQ.0vAo5CbDpyLSu-MT21JAsVYnV1M')