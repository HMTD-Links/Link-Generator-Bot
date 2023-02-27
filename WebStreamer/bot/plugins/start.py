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
from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from handlers.database import Database
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.name)
Broadcast_IDs = {}

################################################################################################################################################################################################################################################
# Start Command

MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😁 Help', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😎 About', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]


@StreamBot.on_message(filters.command("start") & filters.private)
async def start(_, m: Message):
    reply_markup = InlineKeyboardMarkup(MAIN_MENU_BUTTONS)
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
    raise StopPropagation


################################################################################################################################################################################################################################################
# Help Command

HELP_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@StreamBot.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
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

ABOUT_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@StreamBot.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    mention = message.from_user.mention
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
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
# CallBackQuery For Star Message

@StreamBot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        HELP_BUTTON = [
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(HELP_BUTTON)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        GROUP_BUTTONS = [
            [
                InlineKeyboardButton("Star Movies Feedback", url="https://t.me/Star_Movies_Feedback_Bot")
            ],
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(GROUP_BUTTONS)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("👨🏻‍✈️ Admin", url="https://t.me/Star_Movies_Karthik")
            ],
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TUTORIAL_BUTTONS)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        START_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik')
            ],
            [
                InlineKeyboardButton('😁 Help', callback_data="TUTORIAL_CALLBACK"),
                InlineKeyboardButton('👥 Support', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('😎 About', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(START_BUTTONS)
        mention = query.from_user.mention
        try:
            await query.edit_message_text(
                text="<b>Hi 👋🏻 {} ♥️,  Send me a File 📂 to get an Instant Stream link.</b>".format(
                    mention
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        except MessageNotModified:
            pass    
        return
################################################################################################################################################################################################################################################

REPLY_ERROR = """<b>Use This Command as a Reply to any Telegram Message Without any Spaces.</b>"""

################################################################################################################################################################################################################################################
# Broadcast Message 

@Star_Moviess_Tamil.on_message(filters.private & filters.command("broadcast"))
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

@Star_Moviess_Tamil.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂 :- {await db.total_users_count()}\n\nTotal Users with Notification Enabled 🔔 :- {await db.total_notif_users_count()}**",
        quote=True
    )

################################################################################################################################################################################################################################################
# Ban The User

@Star_Moviess_Tamil.on_message(filters.private & filters.command("ban_user"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"**Use This Command to Ban 🛑 any User From the Bot 🤖.\n\nUsage:-\n\n/ban_user user_id ban_duration ban_reason\n\n Example :- /ban_user 1234567 28 You Misused me.\n This Will Ban User with ID `1234567` for `28` Days for the Reason `You Misused me`.**",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"**Banning user {user_id} for {ban_duration} Days for the Reason {ban_reason}.**"

        try:
            await c.send_message(
                user_id,
                f"**You are Banned 🚫 to Use This Bot for {ban_duration} day(s) for the reason __{ban_reason}__ \n\nMessage from the Admin 🤠**",
            )
            ban_log_text += "**\n\nUser Notified Successfully!!**"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"**\n\n ⚠️ User Notification Failed! ⚠️ \n\n`{traceback.format_exc()}`**"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"**Error Occurred ⚠️! Traceback Given below\n\n`{traceback.format_exc()}`**",
            quote=True
        )

################################################################################################################################################################################################################################################
# Unban User

@Star_Moviess_Tamil.on_message(filters.private & filters.command("unban_user"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"**Use this Command to Unban 😃 Any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.**",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "**\n\n✅ User Notified Successfully!! ✅**"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"**\n\n⚠️ User Notification Failed! ⚠️\n\n`{traceback.format_exc()}`**"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"**⚠️ Error Occurred ⚠️! Traceback Given below\n\n`{traceback.format_exc()}`**",
            quote=True,
        )

################################################################################################################################################################################################################################################
# Banned Users

@Star_Moviess_Tamil.on_message(filters.private & filters.command("banned_users"))
async def _banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"> **User ID :- `{user_id}`, Ban Duration :- `{ban_duration}`, Banned on :- `{banned_on}`, Reason :- `{ban_reason}`\n\n**"
    reply_text = f"**Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}**"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)
