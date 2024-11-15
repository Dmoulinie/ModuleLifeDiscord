"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.pingCommand = void 0;
exports.executePing = executePing;
const discord_js_1 = require("discord.js");
exports.pingCommand = new discord_js_1.SlashCommandBuilder()
    .setName('ping')
    .setDescription('Renvoie Pong!');
async function executePing(interaction) {
    await interaction.reply('Pong!');
}
