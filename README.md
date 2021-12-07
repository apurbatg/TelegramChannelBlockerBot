# Telegram Channel Blocker Bot

Channel go away!

---

This bot is used to delete and ban message sent by channel

# How this appears?

The reason this appears please see this [contest](https://core.telegram.org/contest/android-2021-11-api) hosted by Telegram

```
channels.sendAsPeers peers:Vector<Peer> chats:Vector<Chat> users:Vector<User> = channels.SendAsPeers;

...

---functions---

...

channels.getSendAs peer:InputPeer = channels.SendAsPeers;
```

In the contest, Telegram added few new APIs. One of them is `channels.sendAsPeers`.
\
This API can send message as a channel peer.

This changes applied in both Development and Production server,
\
but in Production this behaves were limited. (Only channel admin can send as a channel peer)

Later (07-12-2021), Telegram released a new update that normal user can do the same thing, as they are owner of the channel peer.
\
So this bot is invented to solve this problem.

Currently, (07-12-2021) Telegram didn't add those APIs in the official Schema.

# Install

Pre requirements:
- Python 3.8+ (pypy should also support, but not tested.)

This project uses [poetry](https://python-poetry.org) to install dependencies.
\
Please install poetry globally by using `pip install poetry`

```shell
$ poetry init

Using version ^X.X.X for loguru
Using version ^X.X.X for Pyrogram
Using version ^X.X.X for TgCrypto
...

Updating dependencies
Resolving dependencies...

Writing lock file

Package operations: 8 installs, 0 updates, 0 removals

  • Installing async-lru (X.X.X)
  • Installing colorama (X.X.X)
  • Installing pyaes (X.X.X)
  • Installing pysocks (X.X.X)
  • Installing win32-setctime (X.X.X)
  • Installing loguru (X.X.X)
  • Installing pyrogram (X.X.X)
  • Installing tgcrypto (X.X.X)
...

$
```

# How to use

Rename `config.ini.example` to `config.ini` and edit the config

Simply run this script with `python3 main.py`
\
and add it to your group, it will automatically start working.

**Important note: You have to TURN OFF [privacy mode](https://core.telegram.org/bots#privacy-mode) for your bot via [@BotFather](https://t.me/BotFather) using `/setprivacy` command**

_Note: You must give this bot permission to delete message and ban users._

# Example bot

Running official bot: [@Auto_Block_Channel_Bot](https://t.me/Auto_Block_Channel_Bot)
\
simply add in your group and give `delete message` and `ban` user permission and there you go!

_Linked group will not affect the function_

# Contributing

Please follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) to write code.

Before submitting pull request, please make sure your code is able to run successfully.
