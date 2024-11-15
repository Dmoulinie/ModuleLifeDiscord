import { SlashCommandBuilder, CommandInteraction } from 'discord.js';

export const helloCommand = new SlashCommandBuilder()
    .setName('hello')
    .setDescription('Renvoie Bonjour!');

export async function executeHello(interaction: CommandInteraction) {
    await interaction.reply('Bonjour !');
}