import discord
from discord.ext import commands
import datetime as dt
from config import ANNOUNCEMENTS, GREEN, RED, USCUSTOMER, CACUSTOMER, CACHANNEL, USCHANNEL


class OpenClose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def usopen(self, ctx):
        announcements = self.bot.get_channel(ANNOUNCEMENTS)
        usrole = ctx.guild.get_role(USCUSTOMER)
        channel = self.bot.get_channel(USCHANNEL)
        await channel.edit(name="🟢𝐔𝐒𝐀🟢", reason="US Open Edit. -- command called")
        em = discord.Embed(title="🟢 USA 🟢", description="We are now open for business!", colour=GREEN)
        em.set_footer(text=ctx.guild.name)
        em.set_thumbnail(url="https://cdn.free-printable-signs.com/images/we-are-open-sign.png")
        em.timestamp = dt.datetime.utcnow()
        await announcements.send(f"{usrole.mention}", embed=em)
        await ctx.message.delete(delay=2)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def caopen(self, ctx):
        announcements = self.bot.get_channel(ANNOUNCEMENTS)
        CArole = ctx.guild.get_role(CACUSTOMER)
        channel = self.bot.get_channel(CACHANNEL)
        await channel.edit(name="🟢𝐂𝐀𝐍𝐀𝐃𝐀🟢", reason="CA Open Edit. -- command called")
        em = discord.Embed(title="🟢 Canada 🟢", description="We are now open for business!", colour=GREEN)
        em.set_footer(text=ctx.guild.name)
        em.timestamp = dt.datetime.utcnow()
        em.set_thumbnail(url="https://cdn.free-printable-signs.com/images/we-are-open-sign.png")
        await announcements.send(f"{CArole.mention}", embed=em)
        await ctx.message.delete(delay=2)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def usclose(self, ctx):
        announcements = self.bot.get_channel(ANNOUNCEMENTS)
        usrole = ctx.guild.get_role(USCUSTOMER)
        channel = self.bot.get_channel(USCHANNEL)
        await channel.edit(name="❌𝐔𝐒𝐀❌", reason="US Close Edit. -- command called")
        em = discord.Embed(title="❌ USA ❌", description="We are now closed!", colour=RED)
        em.set_footer(text=ctx.guild.name)
        em.timestamp = dt.datetime.utcnow()
        await announcements.send(f"{usrole.mention}", embed=em)
        await ctx.message.delete(delay=2)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def caclose(self, ctx):
        announcements = self.bot.get_channel(ANNOUNCEMENTS)
        CArole = ctx.guild.get_role(CACUSTOMER)
        channel = self.bot.get_channel(CACHANNEL)
        await channel.edit(name="❌𝐂𝐀𝐍𝐀𝐃𝐀❌", reason="CA Close Edit. -- command called")
        em = discord.Embed(title="❌ Canada ❌", description="We are now closed!", colour=RED)
        em.set_footer(text=ctx.guild.name)
        em.timestamp = dt.datetime.utcnow()
        await announcements.send(f"{CArole.mention}", embed=em)
        await ctx.message.delete(delay=2)


async def setup(bot):
    await bot.add_cog(OpenClose(bot))
