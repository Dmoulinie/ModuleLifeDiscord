"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const discord_js_1 = require("discord.js");
const dotenv_1 = __importDefault(require("dotenv"));
const interactionCreate_1 = __importDefault(require("./events/interactionCreate")); // Gestionnaire des interactions
const ready_1 = __importDefault(require("./events/ready"));
const messageListener_1 = __importDefault(require("./events/messageListener"));
dotenv_1.default.config();
const bot = new discord_js_1.Client({
    intents: [
        discord_js_1.GatewayIntentBits.Guilds,
        discord_js_1.GatewayIntentBits.GuildMessages,
        discord_js_1.GatewayIntentBits.MessageContent,
        discord_js_1.GatewayIntentBits.GuildMembers,
    ],
});
(0, interactionCreate_1.default)(bot);
(0, messageListener_1.default)(bot);
const token = process.env.DISCORD_TOKEN;
if (!token) {
    throw new Error('Le token Discord est manquant dans le fichier .env');
}
bot.once('ready', () => {
    (0, ready_1.default)(bot);
});
bot.login(token);
// bot.once('ready', () => {
//     console.log(`Bot connecté en tant que ${bot.user?.tag}`);
// });
process.on('SIGINT', () => {
    console.log('Arrêt du bot...');
    bot.destroy(); // Ferme proprement la connexion du bot à Discord
    process.exit(0);
});
