import {Client, Message} from 'discord.js';

export default (bot: Client) => {

    bot.on('messageCreate', async (message: Message) => {
        if (message.author.bot) return;

        const words = message.content.trim().split(/\s+/);

        const lastWord = words[words.length - 1]?.toLowerCase();
        if (lastWord === 'quoi') {
            await message.reply('feur');
        }
    });
};