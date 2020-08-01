# imported discord modules
import discord
from discord.ext import commands
from discord.utils import get

# checks if the user who invoked the command has permissions, return otherwise
# manage_channels must be true in order to allow making and managing channels
def can_create():
    async def predicate(ctx):
        member = ctx.message.author
        return member.guild_permissions.manage_channels
    return commands.check(predicate)

# class for storing creation commands
class Creation(commands.Cog):
    # constructor
    def __init__(self, bot):
        self.bot = bot

    # command to create a basic text channel
    @commands.group(invoke_without_command=True)
    @can_create()
    async def create(self, ctx, *, new_channel: str):
        member = ctx.message.author # stores member in a variable
        guild = ctx.guild # stores the guild into a variable

        channel = await guild.create_text_channel(new_channel, overwrites=None, category=guild.categories[1], reason=None)
        await channel.send(f"Text channel {new_channel} was created!")

    # command to create a basic voice channel
    @create.command()
    async def voice(self, ctx, *, new_channel: str):
        member = ctx.message.author
        guild = ctx.guild

        # note: ctx.guild.categories will return a list of possible categories that the server has
        # you can then select where the channel will be created in the category list
        channel = await guild.create_voice_channel(new_channel, overwrites=None, category=guild.categories[2], reason=None)
        await ctx.send(f"Voice channel {new_channel} was created!")

    # command to create a private text channel
    @create.command()
    async def priv(self, ctx, *, new_channel: str):
        member = ctx.message.author
        guild = ctx.guild
        
        # use discord.utils.get() for retrieving and storing a role into variables
        # guild.roles is an iterable, and name is an attribute to search for
        admin = get(guild.roles, name="Supreme Piano Ruler")
        mods = get(guild.roles, name="Black Keys")

        # using a dictionary, permissions can be chosen for the new channel
        # guild.default_role is @everyone, guild.me is the bot itself
        # using admin and mods allows to include them into the new channel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            admin: discord.PermissionOverwrite(read_messages=True),
            mods: discord.PermissionOverwrite(read_messages=True)
        }

        channel = await guild.create_text_channel(new_channel, overwrites=overwrites, category=guild.categories[3], reason=None)
        await channel.send(f"Private text channel {new_channel} was created!")

    # command to create a private voice channel
    @create.command()
    async def priv_voice(self, ctx, *, new_channel: str):
        member = ctx.message.author
        guild = ctx.guild
        
        admin = get(guild.roles, name="Supreme Piano Ruler")
        mods = get(guild.roles, name="Black Keys")

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            admin: discord.PermissionOverwrite(read_messages=True),
            mods: discord.PermissionOverwrite(read_messages=True)
        }

        channel = await guild.create_voice_channel(new_channel, overwrites=overwrites, category=guild.categories[2], reason=None)
        await ctx.send(f"Private voice channel {new_channel} was created!")

    # command to delete a given channel
    @commands.command()
    @can_create()
    async def delete(self, ctx, *, channel_name: str):
        member = ctx.message.author
        guild = ctx.guild

        # using discord.utils.get() and bot.get_all_channels(), you can specify an attribute
        # to search through an iterable, in this case all the channels on a guild
        channel = get(self.bot.get_all_channels(), name=channel_name)
        await channel.delete()

        await ctx.send(f"Channel {channel_name} was deleted!")

# setup method to add bot
def setup(bot):
    bot.add_cog(Creation(bot))