import discord
from discord import Color
from discord.ext import commands
from discord.flags import Intents

# client object
client = commands.Bot(command_prefix='?', intents=discord.Intents.all())
client.remove_command('help')

# runs when bot is online
@client.event
async def on_ready():
    print('Bot online.')

# sends an embed message when a user joins the server
@client.event
async def on_member_join(member: discord.Member):
    channel = discord.utils.get(member.guild.channels, name='welcome')

    embed = discord.Embed(title=f'Welcome to the server {member.display_name},', description='Hope you enjoy your stay!', color=Color.blurple())
    embed.set_thumbnail(url=member.avatar_url)
    
    await channel.send(embed=embed)

# pings the bot
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

# sample embed command
@client.command()
async def help(ctx):
    embed = discord.Embed(title='Help Menu', description='List of all commands', color=Color.blurple())
    embed.add_field(name='Example command', value='?example')

    await ctx.send(embed=embed)

# runs the bot
client.run('BOT TOKEN') 