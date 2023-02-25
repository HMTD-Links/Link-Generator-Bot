from pyrogram import filters
from pyrogram.types import Message

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command("start") & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.'
    )

from pyrogram import Client, filters, enums
from bot import Star_Moviess_Tamil
from config import ADMINS, AUTH_USERS
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from translation import Translation
from pyrogram.errors import MessageNotModified, UserIsBlocked, InputUserDeactivated, FloodWait
import random
import os
import asyncio
import traceback
import base64

from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import vers
from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from WebStreamer.handlers.database import Database
LOG_CHANNEL = WebStreamer.vars.LOG_CHANNEL
AUTH_USERS = WebStreamer.vars.AUTH_USERS
DB_URL = WebStreamer.vars.DB_URL
DB_NAME = WebStreamer.vars.DB_NAME

db = Database(DB_URL, DB_NAME)

################################################################################################################################################################################################################################################
# Start Command

START = "Translation.START"

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

@Star_Moviess_Tamil.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

    chat_id = message.from_user.id
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

@Star_Moviess_Tamil.on_message(start_filter)
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(MAIN_MENU_BUTTONS)
    await message.reply_text(
        text = Translation.START.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    raise StopPropagation


################################################################################################################################################################################################################################################
# Help Command

HELP = "Translation.HELP"

HELP_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    text = Translation.HELP
    reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
    await message.reply_text(
        text = Translation.HELP.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# About Command

ABOUT = "Translation.ABOUT"

ABOUT_BUTTONS = [
            [
                InlineKeyboardButton('👨🏻‍💻 Creator', url='https://t.me/Star_Movies_Karthik'),
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil')
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    text = Translation.ABOUT
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    await message.reply_text(
        text = Translation.ABOUT.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################
# Get Movies with Links 👇🏻

MOVIES = "Translation.MOVIES"

MOVIES_BUTTONS = [
            [
                InlineKeyboardButton('Tamil Movies', url='https://t.me/Star_Moviess_Tamil_Bot?start=Tamil_Movies'),
                InlineKeyboardButton('TV Shows', url='https://t.me/Star_Moviess_Tamil_Bot?start=TV_Shows')
            ],
            [
                InlineKeyboardButton('Hollywood Movies', url='https://t.me/Star_Moviess_Tamil_Bot?start=Hollywood_Movies'),
                InlineKeyboardButton('Collection Movies', url='https://t.me/Star_Moviess_Tamil_Bot?start=Collection_Movies')
            ],
            [
                InlineKeyboardButton('Web Series', url='https://t.me/Star_Moviess_Tamil_Bot?start=Web_Series'),
                InlineKeyboardButton('Cartoon Movies', url='https://t.me/Star_Moviess_Tamil_Bot?start=Cartoon_Movies')
            ],
            [
                InlineKeyboardButton('📢 Update Channel', url='https://t.me/Star_Moviess_Tamil'),
            ]
        ]

@Star_Moviess_Tamil.on_message(filters.command("movies") & filters.private & filters.incoming)
async def movies(client, message):
    text = Translation.MOVIES
    reply_markup = InlineKeyboardMarkup(MOVIES_BUTTONS)
    await message.reply_text(
        text = Translation.MOVIES.format(
                mention = message.from_user.mention
            ),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

################################################################################################################################################################################################################################################

REPLY_ERROR = """<b>Use This Command as a Reply to any Telegram Message Without any Spaces.</b>"""

################################################################################################################################################################################################################################################
# Bot Settings

@Star_Moviess_Tamil.on_message(filters.command("settings"))
async def opensettings(bot, cmd):
    user_id = cmd.from_user.id
    print("Successfully Setted Notifications to {await db.get_notif(user_id)}")
    await cmd.reply_text(
        f"**Here You Can Set Your Settings :-\n\nSuccessfully setted Notifications to {await db.get_notif(user_id)}**",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"Notification  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                        callback_data="notifon",
                    )
                ],
                [InlineKeyboardButton("🚫 Close", callback_data="closeMeh")],
            ]
        ),
    )


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
        text=f"**Total Users 📊 :- {await db.total_users_count()}\n\nNotification Enabled Users 🔔 :- {await db.total_notif_users_count()}**",
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

################################################################################################################################################################################################################################################
# CallBackQuery For Bot Settings

@Star_Moviess_Tamil.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    user_id = query.from_user.id
    if query.data == "notifon":
        notif = await db.get_notif(user_id)
        if notif is True:
            await db.set_notif(user_id, notif=False)
        else:
            await db.set_notif(user_id, notif=True)
        await query.edit_message_text(
            f"**Here You Can Set Your Settings :-\n\nSuccessfully setted Notifications to {await db.get_notif(user_id)}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            f"Notification  {'🔔' if ((await db.get_notif(user_id)) is True) else '🔕'}",
                            callback_data="notifon",
                        )
                    ],
                    [InlineKeyboardButton("🚫 Close", callback_data="closeMeh")],
                ]
            ),
        )
        await query.answer(
            f"Successfully Setted Notifications to {await db.get_notif(user_id)}"
        )
    elif query.data == "closeMeh":
      await query.message.delete(True)

################################################################################################################################################################################################################################################
# CallBackQuery For Star Message

    elif query.data=="HELP_CALLBACK":
        HELP_BUTTON = [
            [
                InlineKeyboardButton("👈🏻 Back", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(HELP_BUTTON)
        try:
            await query.edit_message_text(
                text = Translation.ABOUT.format(
                        mention = query.from_user.mention
                    ),
                disable_web_page_preview=True,
                reply_markup=reply_markup
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
        try:
            await query.edit_message_text(
                text = Translation.SUPPORT.format(
                        mention = query.from_user.mention
                    ),
                disable_web_page_preview=True,
                reply_markup=reply_markup
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
        try:
            await query.edit_message_text(
                text = Translation.HELP.format(
                        mention = query.from_user.mention
                    ),
                disable_web_page_preview=True,
                reply_markup=reply_markup
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
        try:
            await query.edit_message_text(
                text = Translation.START.format(
                        mention = query.from_user.mention
                    ),
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    
        return
