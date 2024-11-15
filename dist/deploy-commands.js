"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const discord_js_1 = require("discord.js");
const dotenv_1 = __importDefault(require("dotenv"));
const ping_1 = require("./commands/ping");
const hello_1 = require("./commands/hello");
const cfq_1 = require("./commands/cfq");
dotenv_1.default.config();
const commands = [
    ping_1.pingCommand.toJSON(),
    hello_1.helloCommand.toJSON(),
    cfq_1.cfqCommand.toJSON()
];
const rest = new discord_js_1.REST({ version: '10' }).setToken(process.env.DISCORD_TOKEN);
(async () => {
    try {
        console.log('Enregistrement des commandes slash...');
        await rest.put(discord_js_1.Routes.applicationGuildCommands(process.env.CLIENT_ID, process.env.GUILD_ID), { body: commands });
        console.log('Commandes slash enregistrées avec succès!');
    }
    catch (error) {
        console.error('Erreur lors de l\'enregistrement des commandes slash:', error);
    }
})();
