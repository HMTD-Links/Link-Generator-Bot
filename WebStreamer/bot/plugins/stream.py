import logging
from pyrogram import filters, errors
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, logger
from WebStreamer.utils import get_hash, get_name, get_file_caption
from WebStreamer.utils.file_properties import get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.file_id import FileId

@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply("You are not <b>allowed to use</b> this <a href='https://github.com/EverythingSuckz/TG-FileStreamBot'>bot</a>.", quote=True)
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    file_hash = get_hash(log_msg, Var.HASH_LENGTH)
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"
    short_link = f"{Var.URL}{file_hash}{log_msg.id}"
    cap = m.caption
    file_name = get_name(log_msg)
    file_caption = get_file_caption(log_msg)
    logger.info(f"Generated link :- {stream_link} for {m.from_user.first_name}")
    try:
        await m.reply_cap(
            text="<b>{}\n➠ Link :- [Click here]({})</b>\n\nshortened: {})".format(
                cap, stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Download Link", url=stream_link)]]
            ),
        )
    except errors.ButtonUrlInvalid:
        await m.reply_cap(
            text="<b>{}\n➠ Link :- [Click here]({})</b>\n\nshortened: {})".format(
                cap, stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
        )
