# discord-c2

A Discord bot that will run the message you send it on the server it's running on.  It will then display standard out and 
standard error.

## Installation:

`pip install -r requirements.txt`

## Usage:

`python c2.py`

## `bot_token.py`

`BOT_TOKEN` requires a Discord Bot Token. 

## `commands.py`

A list of authorized commands for the C2 server to run.

```
AUTHORIZED_COMMANDS = [
    'echo hello'
]
```