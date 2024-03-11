# In the Discord Development portal, Make sure to add the "bot" and "application.commands" scopes in OAuth2 link generator

import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Bot is online and ready to go!')
    await bot.change_presence(activity=discord.Game(name="Testing"), status=discord.Status.online)
                                                    # ^ change to your liking

# NOTE these are testing commands. Feel free to change them or add more.    
@bot.command(description="Sends the bot's latency.") 
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="List of commands")
async def help(ctx):
    help_message = """
    **Command Categories:**
    - /ping

    - /embed

    Feel free to contact the bot owner for additional assistance.
    """

    await ctx.respond(content=help_message)

@bot.command(description="Test the embed command")
async def embed(ctx):
    embed = discord.Embed(
        title='Embed Title',
        description='Embed Description',
        color=discord.Color.blue()
    )

    embed.add_field(name='Field 1', value='Value 1', inline=False)
    embed.add_field(name='Field 2', value='Value 2', inline=True)
    embed.add_field(name='Field 3', value='Value 3', inline=True)

    embed.set_footer(text='Footer Text')

    await ctx.respond(embed=embed)

bot.run("YOUR_BOT_TOKEN")