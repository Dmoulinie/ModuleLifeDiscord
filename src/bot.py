import os
import hikari
import lightbulb
import miru
from dotenv import load_dotenv
import json



import requests
import datetime
from wand.image import Image


#--------------------GLOBAL_PATH--------------------
__FILE_PATH__ = os.path.dirname(os.path.abspath(__file__)) # <--- Absolute path to this file

__PARENT_PATH__ = os.path.dirname(__FILE_PATH__) # <--- Absolute path to the parent directory

__SRC_PATH__ = os.path.join(__PARENT_PATH__, 'src') # <--- Absolute path to the src directory

__ASSETS_PATH__ = os.path.join(__PARENT_PATH__, 'assets') # <--- Absolute path to the assets directory

__CLASS_PATH__ = os.path.join(__PARENT_PATH__, 'classes') # <--- Absolute path to the classes directory


#--------------------OTHER_PATH--------------------
__JSON_PATH__ = os.path.join(__ASSETS_PATH__, 'json') # <--- Absolute path to the json directory

__RESPONSE_PATH__ = os.path.join(__JSON_PATH__, 'response.json') # <--- Absolute path to the response.json file in the json directory

__PLANNING_PATH__ = os.path.join(__ASSETS_PATH__, "planning") # <--- Absolute path to the planning directory



"""
Load the token from the .env file
Load the bot
"""
load_dotenv()
__BOT__ = lightbulb.BotApp(os.getenv('token'),
intents=hikari.Intents.ALL,
) # Token
miru.load(__BOT__)


#--------------------@__BOT__ LISTEN--------------------

@__BOT__.listen(hikari.StartedEvent) # When the bot is ready
async def start_hello(event):
    print("Started...")

"""
Repond au message de l'utilisateur en fonction du response.json
Si le message contient "quoi" alors le bot repond "feur"
"""
@__BOT__.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    if event.content:
        message = event.content.lower()

    if not event.is_human:
        return
    if event.content:
        with open(__RESPONSE_PATH__, 'r') as f:
            switcher = json.load(f)

        response = switcher.get(str(message))
        message = "".join(dict.fromkeys(message))
        if response:
            await event.message.respond(response)
            
        elif "quoi" in message:
            messageLastWord = message.split(" ")[-1]
            listCharacters = ["?", ".", "§", "/", "!", ",", ";", " "]
            for char in listCharacters:
                message = message.replace(char, "")
            #TODO : azequoiaze -> feur (a fix)
            #TODO quooooooi -> pas feur (remove doublon)
            #messageLastWord.find("quoi") != -1 > quoiiiiiiiii -> feur
            #message.endswith("quoi") > quoi -> feur
            if message.endswith("quoi") or messageLastWord.find("quoi") != -1:
                await event.message.respond("feur",)


#--------------------@__BOT__ COMMAND--------------------


@__BOT__.command()
@lightbulb.command("cfq", "Demande ça fait quoi")
# @lightbulb.implements(lightbulb.SlashCommand)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_cfq(ctx : lightbulb.SlashCommand) -> None:
    await ctx.respond("ça fait quoi ? @everyone", mentions_everyone=True)

            
"""
Ajoute une reponse au BOT
-------------------------
Prends en parametre un mot et une reponse
"""
@__BOT__.command() #TODO ajouter un CRUD
@lightbulb.option("reponse", "La réponse du BOT", str, required=True)
@lightbulb.option("declencheur", "Votre mot déclencheur", str, required=True)
@lightbulb.command("ajout", "Vos mots sous ce format : mot / reponse ")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def test(ctx):
    declencheur = ctx.options.declencheur.lower()
    reponse = ctx.options.reponse
    await ctx.respond(str(declencheur)+' : '+ str(reponse))
    with open(__RESPONSE_PATH__, 'r',encoding="utf8") as f:
        switcher = json.load(f)
    switcher[declencheur] = reponse
    with open(__RESPONSE_PATH__, 'w',encoding="utf8") as f:
        json.dump(switcher, f, indent=4, ensure_ascii=False)

@__BOT__.command()
@lightbulb.command("temps", "Donne l'heure")
# @lightbulb.implements(lightbulb.SlashCommand)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_time(ctx : lightbulb.SlashCommand) -> None:
    await ctx.respond(f"il est {datetime.datetime.now()}")


@__BOT__.command()
@lightbulb.option("utc", "Le décalage en UTC", int, required=True)
@lightbulb.command("tempstz", "Donne l'heure en timezone")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_time_utc(ctx : lightbulb.SlashCommand) -> None:
    tz = datetime.datetime.utcnow() + datetime.timedelta(hours=ctx.options.utc)
    await ctx.respond(f"il est {tz}")


def clearPlanningFolder():
    for filename in os.listdir(__PLANNING_PATH__):
        if (filename in ["edt.pdf", "edt.jpeg", "edt0.jpeg", "edt1.jpeg", "edt2.jpeg", "edt3.jpeg", "edt4.jpeg", "edt5.jpeg", "edt6.jpeg", "edt7.jpeg", "edt8.jpeg", "edt9.jpeg"]):
            os.remove(os.path.join(__PLANNING_PATH__, filename))

@__BOT__.command()
@lightbulb.option(
    "semestre",
    "votre semestre.",
    choices=[
        hikari.CommandChoice(name="Semestre 7", value="S7"),
        hikari.CommandChoice(name="Semestre 5", value="S5"),
    ],
    type=str,
)
@lightbulb.option("semaine", "donne l'emploi du temps de la semaine voulu.", type=int, required=False, default=datetime.datetime.now().strftime("%V"))
@lightbulb.command("edt", "Recupere l'emploi du temps")
# @lightbulb.implements(lightbulb.SlashCommand)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def command_edt(ctx : lightbulb.SlashCommand) -> None:
    
    clearPlanningFolder()

    semaineActuelle = int(ctx.options.semaine) # Nombre de la semaine de l'année actuelle
    # recupere le jour actuel 
    # jourActuel = datetime.datetime.now().strftime("%A")
    # if (jourActuel == "Saturday" or jourActuel == "Sunday") and ctx.options.semaine != semaineActuelle : # Si le jour est samedi ou dimanche
    #     semaineActuelle += 1  # Ancienne méthode

    jour_en_utc_11 = int(datetime.datetime.now().weekday() + 1) # Jour actuel en UTC+11 [1-7]
    if (jour_en_utc_11 == 6 or jour_en_utc_11 == 7) and ctx.options.semaine != semaineActuelle : # Si le jour est samedi ou dimanche
        semaineActuelle += 1 

    if str(semaineActuelle)[0] == '0': # Si la semaine est inférieur à 10
        semaineActuelle = semaineActuelle[1:] # Enlever le 0 au début

    semaineDebutUniv = int(semaineActuelle) - 6 # Semaine de l'année universitaire 
    dico = {
        "S7": "https://applis.univ-nc.nc/gedfs/edtweb2/2401310814.{semaineDebutUniv}/PDF_EDT_17435_{semaineActuelle}_2024.pdf",
        "S5": "https://applis.univ-nc.nc/gedfs/edtweb2/2401310810.{semaineDebutUniv}/PDF_EDT_17865_{semaineActuelle}_2024.pdf"
    }


    x = requests.get(dico[ctx.options.semestre].format(semaineDebutUniv=semaineDebutUniv, semaineActuelle=semaineActuelle))
    if (x.status_code == 404):
        await ctx.respond(f"L'emploi du temps n'est pas encore disponible pour la semaine {semaineActuelle}")
        return

    with open(f'{__PLANNING_PATH__}/edt.pdf', 'wb') as f:
        f.write(x.content)
            
    dicoSemestre = {
        "S7": "Semestre 7",
        "S5": "Semestre 5"
    }


    with(Image(filename=f"{__PLANNING_PATH__}/edt.pdf",resolution=200)) as source:
        images=source.sequence
        pages=len(images)
        if pages > 1:
            for i in range(pages):
                images[i].compression_quality = 99
                Image(images[i]).save(filename=__PLANNING_PATH__+f'/edt{i}.jpeg')
            for i in range(pages):
                images[i].compression_quality = 99
                Image(images[i]).save(filename=__PLANNING_PATH__+f'/edt{i}.jpeg')
                embed = hikari.Embed(title="Emploi du temps - MIAGE", description=f"Semaine {semaineActuelle} - {dicoSemestre[ctx.options.semestre]} - Page {i+1}/{pages}", color=0x00FF00)
                embed.set_image(f"{__PLANNING_PATH__}/edt{i}.jpeg")
                await ctx.respond(embed)
        else:
            source.compression_quality = 99
            source.save(filename=f'{__PLANNING_PATH__}/edt.jpeg')

            embed = hikari.Embed(title="Emploi du temps - MIAGE", description=f"Semaine {semaineActuelle} - {dicoSemestre[ctx.options.semestre]}", color=0x00FF00)
            embed.set_image(f"{__PLANNING_PATH__}/edt.jpeg")
            await ctx.respond(embed)
            
    clearPlanningFolder()



dico = {
    "L3 - S7": "17435",
    "L3 - S5": "17865"
}




"""
Start the bot
"""
if __name__ == "__main__":
    __BOT__.run()
