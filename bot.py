import hikari
import os
from dotenv import load_dotenv

load_dotenv()
bot = hikari.GatewayBot(os.getenv('token'), intents=hikari.Intents.ALL) # Token

@bot.listen(hikari.StartedEvent)
async def start_hello(event):
    print("Started...")

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    if event.is_human:
        if event.content:
            switcher = {
                    "yo": "ya",
                    "ya": "yo",
                    "pute": "Salope !",
                    "salope": "Pute !",
                    "tamere": "Ton père !",
                    "tonpere": "Ta mère !",
                    "toncousin": "Ta cousine !",
                    "toncouz": "Ta cousine !",
                    "tacousine": "Ton Cousin !",
                    "tacouz": "Ton Cousin !",
                    "tasoeur": "Ton Frere !",
                    "tonfrere": "Ta Soeur !",
                    "tonpapi": "Ta Grand-Mère !",
                    "tasoeur": "Ton Frère !",
                    "nani": "MAMIE??!",
                    "MAMIE": "Nani?",
                    "oui": "Non",
                    "monf ta pas": "des restants ??",
                    "toncousin": "Ta Cousine !",
                    "tonchien": "Ta Chienne !",
                    "tonchat": "TAchxxxx",
                    "rick": "Roll",
                    ":)": ":(",
                    "iciC": "OUEGOA",
                    "xoxo": "Bisoux",
                    "bisou": "XoXo",
                    ":slight_smile:": ":("

                }

            response = switcher.get(str(event.content).lower())
            if response:
                await event.message.respond(response)
bot.run()