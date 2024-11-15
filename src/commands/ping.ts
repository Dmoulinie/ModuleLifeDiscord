import { SlashCommandBuilder, CommandInteraction  } from 'discord.js';

export const pingCommand = new SlashCommandBuilder()
    .setName('ping')
    .setDescription('Renvoie Pong!');

export async function executePing(interaction: CommandInteraction) {
    await interaction.reply('Pong!');
}