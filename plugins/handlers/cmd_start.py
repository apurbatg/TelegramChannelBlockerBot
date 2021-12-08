from loguru import logger
from pyrogram import Client, types, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from plugins.filters import mod_filters
from plugins.glovar import prefix
from plugins.handlers.cmd_whitelist import get_channel_id


@Client.on_message(filters.private & filters.incoming & ~filters.edited
                   & mod_filters.command(["start"], prefix))
async def cmd_start(client: Client, message: types.Message):
    from plugins.glovar import bot_name

    txt_add_me_2_grp = "Add me to group"
    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text=txt_add_me_2_grp,
                url=f"https://t.me/{bot_name}?startgroup=true"
            )
        ]
    ])
    start_msg = "\n".join((
        "Auto ban channel bot",
        "",
        "How to use:",
        f"1. Press \"{txt_add_me_2_grp}\"",
        f"2. Give @{bot_name} ban user and delete message permission",
        "",
        "Commands:",
        "You can find all available commands with a [/] icon",
        "(Or a icon called Menu)",
        "",
        f"For command usage, do {prefix[0]}help [command]"
    ))
    try:
        await message.reply_text(start_msg, reply_markup=markup)
    except:  # noqa
        logger.exception(f"Start command error for user {message.from_user.id}")
