"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = (bot) => {
    bot.once('ready', () => {
        console.log(`Bot connecté en tant que ${bot.user?.tag}`);
    });
};
