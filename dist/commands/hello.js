"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.helloCommand = void 0;
exports.executeHello = executeHello;
const discord_js_1 = require("discord.js");
exports.helloCommand = new discord_js_1.SlashCommandBuilder()
    .setName('hello')
    .setDescription('Renvoie Bonjour!');
async function executeHello(interaction) {
    await interaction.reply('Bonjour !');
}
