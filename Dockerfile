# Utiliser une image officielle Node.js comme image de base
FROM node:18-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier package.json et installer toutes les dépendances (y compris dev)
COPY package*.json ./

# Installer toutes les dépendances, y compris celles de développement (comme TypeScript)
RUN npm install

# Copier le code source dans le conteneur
COPY . .

# Compiler TypeScript en JavaScript
RUN npm run build

# Commande pour démarrer le bot
CMD ["npm", "start"]
