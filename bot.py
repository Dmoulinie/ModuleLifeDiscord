import os
import hikari
import lightbulb
import miru
from dotenv import load_dotenv
import json


#GLOBAL PATH
__FILE_PATH__ = os.path.dirname(os.path.abspath(__file__))

__SRC_PATH__ = os.path.join(__FILE_PATH__, 'src')

__CLASS_PATH__ = os.path.join(__FILE_PATH__, 'classes')

__RESPONSE_PATH__ = os.path.join(__SRC_PATH__, 'response.json')



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
        await ctx.respond("ça fait quoi ? @everyone", mentions_everyone=True)

@__BOT__.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    if not event.is_human:
        return
    if event.content:
        with open(__RESPONSE_PATH__, 'r') as f:
            switcher = json.load(f)

        response = switcher.get(str(event.content).lower())
        if response:
            await event.message.respond(response)
        elif "quoi" in event.message.content:
            message = str(event.content).lower()
            messageLastWord = message.split(" ")[-1]
            listCharacters = ["?", ".", "§", "/", "!", ",", ";", " "]
            for char in listCharacters:
                message = message.replace(char, "")
            #TODO : azequoiaze -> feur (a fix)
            #TODO quooooooi -> pas feur (remove doublon)
            if message.endswith("quoi") or messageLastWord.find("quoi") != -1:
                await event.message.respond("feur",)
            



@__BOT__.command() #TODO ajouter un CRUD
@lightbulb.option("reponse", "La réponse du BOT", str, required=True)
@lightbulb.option("declencheur", "Votre mot déclencheur", str, required=True)
@lightbulb.command("ajout", "Vos mots sous ce format : mot / reponse ")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def test(ctx):
    declencheur = ctx.options.declencheur
    reponse = ctx.options.reponse
    await ctx.respond(str(declencheur)+' : '+ str(reponse))
    with open(__RESPONSE_PATH__, 'r',encoding="utf8") as f:
        switcher = json.load(f)
    switcher[declencheur] = reponse
    with open(__RESPONSE_PATH__, 'w',encoding="utf8") as f:
        json.dump(switcher, f, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    __BOT__.run()
