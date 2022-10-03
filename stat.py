from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix




@Client.on_message(filters.command("stat", prefix) & filters.me)
async def stat(client: Client, message: Message):
    await message.edit(message.message_id())





# This adds instructions for your module
modules_help["stat"] = {
    "stat": "ну тіпа статистика",
}