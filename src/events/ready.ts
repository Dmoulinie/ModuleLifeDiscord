import { Client } from 'discord.js';

export default (bot: Client) => {
    bot.once('ready', () => {
        console.log(`Bot connecté en tant que ${bot.user?.tag}`);
    });
};
