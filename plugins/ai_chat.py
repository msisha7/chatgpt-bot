# ©️biisal jai shree krishna 😎
import asyncio
import random
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from pyrogram.errors import FloodWait
from info import *
from .db import *
from .fsub import get_fsub


@Client.on_message(filters.command("start") & filters.incoming) # type:ignore
async def startcmd(client: Client, message: Message):
    userMention = message.from_user.mention()
    if await users.get_user(message.from_user.id) is None:
        await users.addUser(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text=f"#New_user_started\n\nUser: {message.from_user.mention()}\nid :{message.from_user.id}",
        )
    if FSUB and not await get_fsub(client, message):return
    rm = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("✨Click to view Terabox Video", web_app=WebAppInfo(url=f"https://devbotstbd.netlify.app"))
        ]] 
    )
    k = await message.reply_photo(# type:ignore
        photo="https://graph.org/file/2e454fc046ea16675451c-1f8167df679f40f92c.jpg",
        caption=f"<b>Hey {userMention},\n\nIᴍ Hᴇʀᴇ Tᴏ Rᴇᴅᴜᴄᴇ Yᴏᴜʀ Pʀᴏʙʟᴇᴍs..\nYou can use me to view terabox content for free\n\nMʏ Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/Champaklalbot>Champaklal</a>\nMʏ Lᴏᴠᴇʀ : <a href=tg://settings/>Tʜɪs Pᴇʀsᴏɴ</a></b>",
        reply_markup=rm,
    )
    await asyncio.sleep(300)
    await k.delete()
    return


@Client.on_message(filters.command("broadcast") & (filters.private) & filters.user(ADMIN)) # type:ignore
async def broadcasting_func(client : Client, message: Message):
    msg = await message.reply_text("Wait a second!") # type:ignore
    if not message.reply_to_message:
        return await msg.edit("<b>Please reply to a message to broadcast.</b>")
    await msg.edit("Processing ...")
    completed = 0
    failed = 0
    to_copy_msg = message.reply_to_message
    users_list = await users.get_all_users()
    for i , userDoc in enumerate(users_list):
        if i % 20 == 0:
            await msg.edit(f"Total : {i} \nCompleted : {completed} \nFailed : {failed}")
        user_id = userDoc.get("user_id")
        if not user_id:
            continue
        try:
            await to_copy_msg.copy(user_id , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎭 ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ 🎗️", url='https://t.me/bisal_files_talk')]]))
            completed += 1
        except FloodWait as e:
            if isinstance(e.value , int | float):
                await asyncio.sleep(e.value)
                await to_copy_msg.copy(user_id , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎭 ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ 🎗️", url='https://t.me/bisal_files_talk')]]))
                completed += 1
        except Exception as e:
            print("Error in broadcasting:", e) 
            failed += 1
            pass
    await msg.edit(f"Successfully Broadcasted\nTotal : {len(users_list)} \nCompleted : {completed} \nFailed : {failed}")
    
