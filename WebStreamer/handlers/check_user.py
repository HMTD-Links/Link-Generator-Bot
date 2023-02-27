import datetime

from WebStreamer.vars import Var
import logging

from WebStreamer.handlers.database import Database

DB_URL = Var.DB_URL
DB_NAME = Var.DB_NAME
LOG_CHANNEL = Var.LOG_CHANNEL

db = Database(DB_URL, DB_NAME)

async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"**#New_User :- \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n ID :- {message.from_user.id} Started @{BOT_USERNAME} !!**",
            )
        else:
            logging.info(f"#New_User :- Name : {cmd.from_user.first_name} ID : {cmd.from_user.id}")

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        print(ban_status)
        if (
            datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("**You are Banned to Use This Bot**", quote=True)
            return
    await cmd.continue_propagation()
