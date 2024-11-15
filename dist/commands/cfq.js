"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.cfqCommand = void 0;
exports.executeCfq = executeCfq;
const discord_js_1 = require("discord.js");
exports.cfqCommand = new discord_js_1.SlashCommandBuilder()
    .setName('cfq')
    .setDescription('Demande ça fait quoi !');
async function executeCfq(interaction) {
    await interaction.reply({
        content: 'ça fait quoi ? @everyone',
        allowedMentions: { parse: ['everyone'] }
    });
}
