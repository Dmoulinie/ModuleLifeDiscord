import { REST, Routes } from 'discord.js';
import dotenv from 'dotenv';
import { pingCommand } from './commands/ping';
import { helloCommand } from './commands/hello';
import {cfqCommand} from "./commands/cfq";

dotenv.config();

const commands = [
    pingCommand.toJSON(),
    helloCommand.toJSON(),
    cfqCommand.toJSON()
];

const rest = new REST({ version: '10' }).setToken(process.env.DISCORD_TOKEN!);

(async () => {
    try {
        console.log('Enregistrement des commandes slash...');

        await rest.put(
            Routes.applicationGuildCommands(process.env.CLIENT_ID!, process.env.GUILD_ID!),
            { body: commands }
        );

        console.log('Commandes slash enregistrées avec succès!');
    } catch (error) {
        console.error('Erreur lors de l\'enregistrement des commandes slash:', error);
    }
})();
