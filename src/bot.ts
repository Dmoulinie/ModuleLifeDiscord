import { Client, GatewayIntentBits } from 'discord.js';
import dotenv from 'dotenv';
import loadInteractionCreate from './events/interactionCreate';  // Gestionnaire des interactions
import loadEventsReady from './events/ready';
import loadFeurListener from './events/feurListener';
import loadFeurKaruta from './events/karutaListener';

dotenv.config();

const bot = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers,
    ],
});

loadInteractionCreate(bot);
loadFeurListener(bot);
loadFeurKaruta(bot);

const token = process.env.DISCORD_TOKEN;
if (!token) {
    throw new Error('Le token Discord est manquant dans le fichier .env');
}

bot.once('ready', () => {
    loadEventsReady(bot);
});

bot.login(token);

// bot.once('ready', () => {
//     console.log(`Bot connecté en tant que ${bot.user?.tag}`);
// });


process.on('SIGINT', () => {
    console.log('Arrêt du bot...');
    bot.destroy();  // Ferme proprement la connexion du bot à Discord
    process.exit(0);
});