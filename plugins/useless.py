import time
from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper_func import get_readable_time
from database import db  # make sure this is correctly imported based on your setup

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)

    # Get the stats from your database
    users = await db.total_users_count()
    files = await db.total_files_count()

    # Now pass all required variables
    await message.reply(BOT_STATS_TEXT.format(users=users, files=files, uptime=uptime))

@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
