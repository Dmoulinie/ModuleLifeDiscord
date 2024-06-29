# ModuleLifeDiscord

## On verifie que le service docker est start

## Todo pour semestre 6 

- Aller sur emploit du temps unc
- Récuperer le lien des pdf du semestre 6 par le network
- Rajouter choice dans option du semestre
- Rajouter la clé "S6" dans la variable dico

## On build l'image du bot :
### A la racine du projet tu fais :

```
sudo docker build -t bot .
```

## Pour lancer le bot en mode détaché tu fais:

```
docker run -d bot
```

## Pour rentrer dans le docker sous linux en CLI:

```
sudo docker exec -it $(sudo docker ps -q --filter ancestor=bot) sh
```
