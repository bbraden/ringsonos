from discord.ext import commands

from ringGUI import *

import sys

from consoleColors import bcolors

client = commands.Bot(command_prefix=".")

readyDiscMsg = """disc ready"""

@client.event
async def on_ready():
    print(readyDiscMsg)


@client.command(aliases=['allring', 'all'])
async def ringall(ctx):
    ring_all()
    await ctx.send(":bell: Successfully Rung Braden's Doorbell.")


@client.command(aliases=['test', 'alltest'])
async def ringtest(ctx):
    ring_all_test()
    await ctx.send(":bell: Successfully Rung Braden's Doorbell. (test)")


@client.command(aliases=['doorbellring', 'doorbell'])
async def ringdoorbell(ctx):
    ring_ring()
    await ctx.send(""":bell: Successfully Rung Braden's Doorbell.""")


@client.command(aliases=['chimesring', 'chimes'])
async def ringchimes(ctx):
    ring_chimes()
    await ctx.send(""":bell: Successfully Rung Braden's Doorbell.""")

@client.command(aliases=['stopbot'])
async def stop():
    sys.exit()


client.run("ODk3MzQ1NDI3MTEwNzg5MTQy.YWUUDQ.vSRqR1XQrlnnWkQXV6YUSAYE3pY")
