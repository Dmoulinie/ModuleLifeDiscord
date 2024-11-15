import {Client, Message} from 'discord.js';

export default (bot: Client) => {

    const targetBotId = '646937666251915264'; // karuta ID

    bot.on('messageCreate', async (message: Message) => {
        if (message.author.bot) return;

        const words = message.content.trim().split(/\s+/);

        const lastWord = words[words.length - 1]?.toLowerCase();
        if (lastWord === 'quoi') {
            await message.reply('feur');
        }


        const messageContent = "I'm dropping 3 cards since this server is currently active!";
        if (message.author.id === targetBotId && message.content === messageContent) {
            await message.reply({
                    content: ' Karuta drop rdm @everyone',
                    allowedMentions: {parse: ['everyone']}
                });
        }



    });
};