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

A list of authorized commands for the C2 server to run and to set a bypass code to allow for you to run commands with
"authentication." `BYPASS_CODE` ***IS*** case-sensitive.

```
AUTHORIZED_COMMANDS = [
    'echo hello'
]

BYPASS_CODE = 'ABC'
```

BYPASS_CODE example:  

```
COMMAND: ABC echo goodbye  
RESPONSE: goodbye
COMMAND: echo goodbye
RESPONSE: Not an authorized command.
```