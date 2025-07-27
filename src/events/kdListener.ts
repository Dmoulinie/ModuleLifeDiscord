import {Client, Message, ChannelType} from 'discord.js';

export default (bot: Client) => {

    bot.on('messageCreate', async (message: Message) => {
        if (message.author.bot) return;

        // Vérifier que le salon n'a pas "karuta" dans son nom
        if (message.channel && (message.channel.type === ChannelType.GuildText || message.channel.type === ChannelType.DM)) {
            const channelName = message.channel.type === ChannelType.GuildText ? message.channel.name : '';
            if (channelName.toLowerCase().includes('karuta')) {
                return;
            }
        }

        const words = message.content.trim().split(/\s+/);

        const lastWord = words[words.length - 1]?.toLowerCase();
        if (lastWord === 'kd') {
            await message.reply(`${message.author.displayName || message.author.username} s'est trompé de salon !!!!! AHAHAHA le nul`);
        }
    });
};