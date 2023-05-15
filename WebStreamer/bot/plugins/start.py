from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from WebStreamer.handlers.broadcast import broadcast
from WebStreamer.handlers.database import Database
from WebStreamer.handlers.check_user import handle_user_status
from pyrogram.types import Message
LOG_CHANNEL = Var.LOG_CHANNEL
AUTH_USERS = Var.AUTH_USERS
DB_URL = Var.DB_URL
DB_NAME = Var.DB_NAME
OWNER_ID = Var.OWNER_ID

db = Database(DB_URL, DB_NAME)


################################################################################################################################################################################################################################################
# Start Command

STAR_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', user_id=OWNER_ID)
            ],
            [
                InlineKeyboardButton('🤖 Bot Channel', url='https://t.me/Star_Bots_Tamil'),                        
                InlineKeyboardButton('👥 Support Group', url='https://t.me/Star_Bots_Tamil_Support')
            ]
        ]

@StreamBot.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"**#New_User :- \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n ID :- {message.from_user.id} Started @{BOT_USERNAME} !!**",
            )
        else:
            logging.info(f"New User :- Name :- {message.from_user.first_name} ID :- {message.from_user.id}")

@StreamBot.on_message(filters.command(["start"]) & filters.private)
async def start(_, m: Message):
    reply_markup = InlineKeyboardMarkup(STAR_BUTTONS)
    mention = m.from_user.mention(style="md")
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "<b>You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.</b>",
            disable_web_page_preview=True, quote=True
        )
    await m.reply_text(
            text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )



################################################################################################################################################################################################################################################
# Help Command


@StreamBot.on_message(filters.command(["help"]) & filters.private & filters.incoming)
async def help(client, message):
    reply_markup = InlineKeyboardMarkup(STAR_BUTTONS)
    mention = message.from_user.mention
    if Var.ALLOWED_USERS and not ((str(message.from_user.id) in Var.ALLOWED_USERS) or (message.from_user.username in Var.ALLOWED_USERS)):
        return await message.reply(
            "<b>You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.</b>",
            disable_web_page_preview=True, quote=True
        )
    await message.reply_text(
            text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )

################################################################################################################################################################################################################################################
# About Command


@StreamBot.on_message(filters.command(["about"]) & filters.private & filters.incoming)
async def about(client, message):
    mention = message.from_user.mention
    reply_markup = InlineKeyboardMarkup(STAR_BUTTONS)
    if Var.ALLOWED_USERS and not ((str(message.from_user.id) in Var.ALLOWED_USERS) or (message.from_user.username in Var.ALLOWED_USERS)):
        return await message.reply(
            "<b>You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.</b>",
            disable_web_page_preview=True, quote=True
        )
    await message.reply_text(
            text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                mention
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )



################################################################################################################################################################################################################################################

REPLY_ERROR = """<b>Use This Command as a Reply to any Telegram Message Without any Spaces.</b>"""

################################################################################################################################################################################################################################################
# Broadcast Message 

@StreamBot.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.reply(REPLY_ERROR, quote=True)
    else:
        await broadcast(m, db)

################################################################################################################################################################################################################################################
# Total Users in Database 📂

@StreamBot.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂 :- {await db.total_users_count()}**",
        quote=True
    )
