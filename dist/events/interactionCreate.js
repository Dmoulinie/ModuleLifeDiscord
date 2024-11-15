"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ping_1 = require("../commands/ping");
const hello_1 = require("../commands/hello");
const cfq_1 = require("../commands/cfq");
exports.default = (bot) => {
    bot.on('interactionCreate', async (interaction) => {
        if (!interaction.isCommand())
            return;
        switch (interaction.commandName) {
            case 'ping':
                await (0, ping_1.executePing)(interaction);
                break;
            case 'hello':
                await (0, hello_1.executeHello)(interaction);
                break;
            case 'cfq':
                await (0, cfq_1.executeCfq)(interaction);
                break;
            default:
                await interaction.reply('Commande non reconnue.');
        }
    });
};
