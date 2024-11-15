import {Client, Interaction} from 'discord.js';
import { executePing } from '../commands/ping';
import { executeHello } from '../commands/hello';
import {executeCfq} from "../commands/cfq";

export default (bot: Client) => {
    bot.on('interactionCreate', async (interaction: Interaction) => {
        if (!interaction.isCommand()) return;

        switch (interaction.commandName) {
            case 'ping':
                await executePing(interaction);
                break;

            case 'hello':
                await executeHello(interaction);
                break;

            case 'cfq':
                await executeCfq(interaction);
                break;

            default:
                await interaction.reply('Commande non reconnue.');
        }
    });
};