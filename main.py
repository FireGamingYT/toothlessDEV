import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='/=', description='a simple test bot')

@bot.event
async def on_ready():
    activity = discord.Game(name="with tennis balls | =help", type=2)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Toothless dev is ready ^-^")
    print(f"Toothless dev is currently in {len(bot.guilds)} guilds")
    print('Bot has started successfully')

@bot.command(name="ping", aliases=["latency", "ms"], brief="Shows latency from bot")
async def ping(ctx):
  embed=discord.Embed(title="ping", description="ToothlessDEV latency", color=0x00ff00)
  embed.add_field(name="Ping:", value=f'**{bot.latency:.2f}**ms')
  await ctx.send(embed=embed)

@bot.command(name="invite", aliases=["inv"], brief="Shows the bot's oauth link")
async def invite(ctx):
  embed=discord.Embed(title="Toothless DEV invite", description="For private use only", color=0x00ff00)
  embed.add_field(name="Invite link", value="https://discord.com/api/oauth2/authorize?client_id=707216713581592631&permissions=8&scope=bot", inline=True)
  await ctx.send(embed=embed)

@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")
async def statistics(ctx):
	embed=discord.Embed(title="Statistics Toothless:", description="Global Bot Statistics", color=0x00ff00)
	embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
	embed.add_field(name="Total users", value=len(bot.users), inline=False)
	embed.add_field(name="More:", value="Coming soon...", inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def get_id(ctx, member: discord.Member):
  user_id = member.id
  await ctx.send('The user id is %d.' % user_id)
  
@bot.command(aliases=['av'])
async def avatar(ctx, *, user: discord.Member=None):
    if user is None:
      user = ctx.author
    else:
      user = user
      
      eA = discord.Embed(title='Avatar', 
      color=discord.Color.green())
      eA.set_author(name=user, icon_url=user.avatar_url)
      eA.set_image(url=user.avatar_url)
      await ctx.send(embed=eA)

import config

bot.run(config.token)