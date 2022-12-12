import os
import hikari
import lightbulb
import miru
from dotenv import load_dotenv


load_dotenv()
__BOT__ = lightbulb.BotApp(os.getenv('token'),
intents=hikari.Intents.ALL,
) # Token
miru.load(__BOT__)

@__BOT__.listen(hikari.StartedEvent) # When the bot is ready
async def start_hello(event):
    print("Started...")


@__BOT__.command()
@lightbulb.option("text", "Le texte a dire", str, required=True)
@lightbulb.command("say", "Dit ce que tu veux")
# @lightbulb.implements(lightbulb.SlashCommand)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_say(ctx : lightbulb.SlashCommand) -> None:
    await ctx.respond(ctx.options.text)



@__BOT__.command()
@lightbulb.command("cfq", "Demande ça fait quoi")
# @lightbulb.implements(lightbulb.SlashCommand)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_cfq(ctx : lightbulb.SlashCommand) -> None:
    await ctx.respond("ça fait quoi ? @everyone",mentions_everyone=True)
    # await ctx.respond("ça fait quoi ?" + ctx.user.default_role.mention)

@__BOT__.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    if not event.is_human:
        return
    if event.content:
        switcher = {
                "yo": "ya",
                "ya": "yo",
                "pute": "salope !",
                "salope": "pute !",
                "tamere": "ton père !",
                "tonpere": "ta mère !",
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
                "oui": "non",
                "non": "oui",
                "monf ta pas": "des restants ??",
                "toncousin": "Ta Cousine !",
                "tonchien": "Ta Chienne !",
                "tonchat": "TAchxxxx",
                "rick": "Roll",
                ":)": ":(",
                "iciC": "OUEGOA",
                "xoxo": "Bisoux",
                "bisou": "XoXo",
                ":slight_smile:": ":(",
            }

        response = switcher.get(str(event.content).lower())
        if response:
            await event.message.respond(response)
        elif "quoi" in event.message.content:
            message = str(event.content).lower()
            listCharacters = ["?", ".", "§", "/", "!", ",", ";", " "]
            for char in listCharacters:
                message = message.replace(char, "")
            if message.endswith("quoi"):
                await event.message.respond("feur",)

if __name__ == "__main__":
    __BOT__.run()