import discord

async def send_message(interaction: discord.Interaction, message: str): 
    await interaction.followup.send(f"{message}")
    return