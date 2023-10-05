import traceback
import random
import colorsys
import discord
import defer
import datetime
from datetime import timedelta
from datetime import datetime
from discord import app_commands
from discord import embeds
from discord import colour
from discord import *
from discord import ui
from discord.ext import *
from discord.ext import commands, tasks
from discord import Client, Intents
import os
import time
import pyrandmeme
from pyrandmeme import *
import requests
import re
import traceback



#Bot Setup
intents = discord.Intents.all()
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@client.listen('on_message')
async def f4(message):
    print(f"{str(message.author)} in {message.guild.name}: {message.content}")

@client.event
async def on_ready():
    # this runs when the account is logged into
    print("We have logged in as {0.user}".format(client))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)    

#whitelist

TEST_GUILD = discord.Object(1152621828641140796)


class MyClient(discord.Client):
    def __init__(self) -> None:
        # Just default intents and a `discord.Client` instance
        # We don't need a `commands.Bot` instance because we are not
        # creating text-based commands.
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def setup_hook(self) -> None:
        # Sync the application command with Discord.
        await self.tree.sync(guild=TEST_GUILD)


class Feedback(discord.ui.Modal, title='Whitelist'):
    # Our modal classes MUST subclass `discord.ui.Modal`,
    # but the title can be whatever you want.

    # This will be a short input, where the user can enter their name
    # It will also have a placeholder, as denoted by the `placeholder` kwarg.
    # By default, it is required and is a short-style input which is exactly
    # what we want.
    name = discord.ui.TextInput(
        label=' IG Name | Nom en jeu',
        placeholder='Your IG name here... | Votre nom en jeu ici...',
    )

    # This is a longer, paragraph style input, where user can submit feedback
    # Unlike the name, it is not required. If filled out, however, it will
    # only accept a maximum of 300 characters, as denoted by the
    # `max_length=300` kwarg.
    feedback = discord.ui.TextInput(
        label='Infos?',
        style=discord.TextStyle.long,
        placeholder='Type your infos here (hours in the game , when did you started...) | Taper vos infos ici)',
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your request | Merci de votre demande , {self.name.value}!', ephemeral=True)
        with open("whitelist.txt", "a") as my_file:
            my_file.write(f"|{self.name.value} | {self.feedback.value} |")
            my_file.close()

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)



client = MyClient()


@client.tree.command(guild=TEST_GUILD, description="Whitelist")
async def whitelist(interaction: discord.Interaction):
    # Send the modal with an instance of our `Feedback` class
    # Since modals require an interaction, they cannot be done as a response to a text command.
    # They can only be done as a response to either an application command or a button press.
    await interaction.response.send_modal(Feedback())



client.run('MTE1MzczMjQyODI2ODA2MDcwMw.GUyjtA.qR4f06ogHEY12z7h18_hVM0n6kumUBp7JcYcpw')