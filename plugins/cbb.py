#(©) PythonBotz 

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b><blockquote>╭───────────⍟
├➤ ᴏᴡɴᴇʀ : <a href='t.me/Momo_Ayase_bot>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
├➤ ʟɪʙʀᴀʀy : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
├➤ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
├➤ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/AniHorizon>AniHorizon</a>
├➤ ᴘᴀɪᴅ ʙᴏᴛ : <a href=https://t.me/Tharun_stryker>ʀ ᴇ ᴏ ɴ</a>
├➤ ᴅᴇᴠʟᴏᴘᴇʀ : <a href=https://t.me/Momo_Ayase_bot>🇸 🇹 🇷 🇾 🇰 🇪 🇷 </a>
╰───────────────⍟</blockquote></b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data ="source"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , callback_data = "main")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ live action 𝟷𝟾+ ᴠɪᴅᴇᴏs", url = "https://t.me/+MzzvhcCIVzg0NDY1")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
       

        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "main":
        await query.message.edit_text(
            text=f"<blockquote>ʜᴇʟʟᴏ ᴍʏ ᴜsᴇʀs ᴍʏ ᴜᴘᴅᴀᴛᴇ & ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+fFiQg-aN1XU0YWZl"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url = "t.me/AniHorizon")
                    ],
                    [   InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"), 
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"<b><blockquote>ʜᴇʏ !! {query.from_user.mention}\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton(text="🏖️", callback_data="about"),
                    InlineKeyboardButton(text="🍂", callback_data="about"),
                    InlineKeyboardButton(text="⚠️", callback_data="me"),
                    InlineKeyboardButton(text="💸", callback_data="about"),
                    InlineKeyboardButton(text="🎭", callback_data="about"),
                ],[ InlineKeyboardButton( "ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", callback_data = "main" ),
                    InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ", callback_data = "source")
                ], [ InlineKeyboardButton("ᴡᴀᴛᴄʜ 𝟷𝟾+ live action ᴠɪᴅᴇᴏs", url = "https://t.me/+MzzvhcCIVzg0NDY1") ],
                [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
    elif data == "me":
            await query.message.edit(
                text=f"<b>ᴛʜɪs sᴇᴄᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs & ᴅᴇᴠᴇʟᴏᴘᴇʀ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [  InlineKeyboardButton("ᴅᴇᴠʟᴏᴘᴇʀ",url= "t.me/Tharun_stryker"),
                         InlineKeyboardButton("ᴀᴅᴍɪɴ",url = "t.me/Momo_Ayase_bot")],
                        [ InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data = "home"),
                         InlineKeyboardButton( "🚫 ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
         )

    elif data == "source":
        await query.message.edit_text(
            text=f"<b><blockquote>ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ\nɪɴ ᴛᴡᴏ ᴡᴀʏs\n★ <a herf='https://t.me/+JBlEWX_WzR45MTc9'>ɢɪᴛʜᴜʙ</a> \n★ <a herf='https://t.me/+JBlEWX_WzR45MTc9'>ᴢɪᴘ ғɪʟᴇ </a></blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ɢɪᴛʜᴜʙ ", url="https://t.me/+JBlEWX_WzR45MTc9"),
                        InlineKeyboardButton("ᴢɪᴘ ғɪʟᴇ",url="https://t.me/+JBlEWX_WzR45MTc9")
                    ],
                    [   InlineKeyboardButton("🔙 ʙᴀᴄᴋ" , callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
                                            )
