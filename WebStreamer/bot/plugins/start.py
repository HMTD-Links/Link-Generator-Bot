from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

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
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
            f"Hi 👋🏻 {m.from_user.mention} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
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
    await message.reply(
            f"Hi 👋🏻 {m.from_user.mention(style="md")} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
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
    text = ABOUT
    reply_markup = InlineKeyboardMarkup(ABOUT_BUTTONS)
    await message.reply(
            f"Hi 👋🏻 {m.from_user.mention(style="md")} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
        )

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
            await query.edit_message(
                f"Hi 👋🏻 {m.from_user.mention} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
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
                f"Hi 👋🏻 {m.from_user.mention(style="md")} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
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
            await query.edit_message(
                f"Hi 👋🏻 {m.from_user.mention(style="md")} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
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
            await query.edit_message(
                f"Hi 👋🏻 {m.from_user.mention(style="md")} ♥️,  Send me a File 📂 to get an Instant Stream link.",
            disable_web_page_preview=True, reply_markup=reply_markup, quote=True
        )
        except MessageNotModified:
            pass    
        return
