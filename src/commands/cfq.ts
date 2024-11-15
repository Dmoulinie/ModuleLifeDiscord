import { SlashCommandBuilder, CommandInteraction  } from 'discord.js';

export const cfqCommand = new SlashCommandBuilder()
    .setName('cfq')
    .setDescription('Demande ça fait quoi !');

export async function executeCfq(interaction: CommandInteraction) {
    await interaction.reply({
        content: 'ça fait quoi ? @everyone',
        allowedMentions: { parse: ['everyone'] }
    });
}