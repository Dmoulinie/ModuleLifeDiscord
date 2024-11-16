import {Client, Message} from 'discord.js';

export default (bot: Client) => {
    const targetBotId = '646937666251915264';// karuta ID
    const messageContent = "I'm dropping 3 cards since this server is currently active!";

    bot.on('messageCreate', async (message: Message) => {
            if (message.author.id === targetBotId && message.content === messageContent) {
                console.log(`Message reçu: ${message.content} de ${message.author.id}`);
                await message.reply({
                    content: ' Karuta drop rdm @everyone',
                    allowedMentions: {parse: ['everyone']}
                }).catch(err=>console.error('erreur lors de l\'envoie du message', err));
            }
        }
    );
}