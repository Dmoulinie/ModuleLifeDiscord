# ModuleLifeDiscord

## Local

### Installation

1. Clone:
    ```
    git clone <repository-url>
    cd ModuleLifeDiscord
    ```

2. Installer les dépendances:
    ```
    npm install
    ```

3. Copier le `.env.copy` en `.env` et éditer les champs:
    ```dotenv
    DISCORD_TOKEN=your_discord_token
    CLIENT_ID=your_client_id
    GUILD_ID=your_guild_id
    ```

4. Compuler le code:
    ```
    npm run build
    ```

5. Lancer le bot:
    ```
    npm run start
    ```
**Note:**  Pour les /commands : `npx ts-node src/deploy-commands.ts` pour les déployer manuellement


## Prod

### Installation avec docker-compose

1. Clone:
    ```
    git clone <repository-url>
    cd ModuleLifeDiscord
    ```
2. Copier le `.env.copy` en `.env` et éditer les champs:
    ```dotenv
    DISCORD_TOKEN=your_discord_token
    CLIENT_ID=your_client_id
    GUILD_ID=your_guild_id
    ```
    
3. Installer les dépendances:
    ```
    npm install
    ```
    
4. Compuler le code:
    ```
    npm run build
    ```

5. Lancer le bot:
    ```
    docker-compose up -d
    ```
    ou
    ```
    docker compose up -d
    ```

**Note** Pour rentrer dans le container & sync les / commands:
```
docker compose exec bot sh
```

```
npx ts-node src/deploy-commands.ts
```


## Todo pour semestre 6

- Aller sur emploit du temps unc
- Récuperer le lien des pdf du semestre 6 par le network
- Rajouter choice dans option du semestre
- Rajouter la clé "S6" dans la variable dico
