import logging
from pyrogram import filters, errors
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.utils import get_hash, get_name
from WebStreamer.utils.file_properties import get_name, get_media_file_size
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.file_id import FileId
from pyromod import listen
from WebStreamer.bot import StreamBot
from WebStreamer.utils.human_readable import humanbytes

links = []
@StreamBot.on_message(filters.private & filters.command("multi"))
async def multi_files(bot, msg):
    if Var.ALLOWED_USERS and not ((str(msg.from_user.id) in Var.ALLOWED_USERS) or (msg.from_user.username in Var.ALLOWED_USERS)):
        return await msg.reply(
            "<b>You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.</b>",
            disable_web_page_preview=True, quote=True
        )
    try : 
      reciv = await bot.ask(msg.chat.id,"**Hit /multi When You Finish Sending Your Files 📂**")
      log_msg = await msg.forward(chat_id=Var.BIN_CHANNEL)
      stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"
      file_hash = get_hash(log_msg, Var.HASH_LENGTH)
      file_caption = msg.caption
      links.append(stream_link)
      if reciv.text =="/multi":
          text = " "
          for i in links :
              text+=f"{i}\n\n"
          await msg.reply(f"**Download Links **\n{file_caption}\n\n{text}")  
          links.clear()
      else : 
          await multi_files(bot, msg)
    except Exception as error:
       await msg.reply(error)
        

       
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
        return await m.reply("**You are not <b>allowed to use</b> this <a href='https://github.com/EverythingSuckz/TG-FileStreamBot'>bot</a>.**", quote=True)
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    file_hash = get_hash(log_msg, Var.HASH_LENGTH)
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"
    short_link = f"{Var.URL}{file_hash}{log_msg.id}"
    file_caption = m.caption
    file_name = get_name(log_msg)
    file_size = humanbytes(get_media_file_size(m))
    logging.info(f"Generated link :- {stream_link} for {m.from_user.first_name}")
    try:
        await m.reply_text(
            text="<b>File Name :- {}\nFile Size :- {}\nFile Captain :- {}\n➠ Link :- [Click here]({})</b>\n<b>(<a href='{}'>Shortened</a>)</b>".format(
                file_name, file_size, file_caption, stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📥 Download Link", url=stream_link)], [InlineKeyboardButton("🔗 Shortened Link", url=short_link)], [InlineKeyboardButton("🔥 Update Channel", url="https://t.me/Star_Moviess_Tamil")]]
            ),
        )
    except errors.ButtonUrlInvalid:
        await m.reply_text(
            text="<b>File Name :- {}\nFile Size :- {}\nFile Captain :- {}\n➠ Link :- [Click here]({})</b>\n<b>(<a href='{}'>Shortened</a>)</b>".format(
                file_name, file_size, file_caption, stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
        )
