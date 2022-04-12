import discord
from discord.ext import commands
import datetime as dt
from config import ANNOUNCEMENTS, GREEN, RED, USCUSTOMER, CACUSTOMER


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def cdelete(self, ctx):
        channels = ctx.channel.category.channels
        for x in channels:
            await x.delete(reason="Category delete! -- command called")
        await ctx.channel.category.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def price(self, ctx, initcost1: float, percent, thrvar: float, tip: float = 0):
        await ctx.message.delete()
        percentage = percent
        percent = float(percent)
        percent = percent / 100
        twpf = initcost1 - (initcost1 * percent)
        twpf = round(twpf, 2)
        total = twpf + thrvar
        total = round(total, 2)
        if tip == 0:
            await ctx.channel.send(f"{initcost1:.2f}-{percentage}% = {twpf:.2f}+{thrvar:.2f}(Taxes&Fees)={total:.2f}")
        else:
            await ctx.channel.send(f"{initcost1:.2f}-{percentage}% = {twpf:.2f}+{thrvar:.2f}(Taxes&Fees)+{tip}(Tip)"
                                   f"={total+tip:.2f}")

async def setup(bot):
    await bot.add_cog(Tickets(bot))
