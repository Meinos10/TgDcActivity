import discord
from discord.ext import commands
from config import *
import asyncio
from pyrogram import Client
from pyrogram.errors import *


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
	activity = discord.Game(name="t.me/ReWoxi", type=3)
	await bot.change_presence(status=discord.Status.idle, activity=activity)
	print("Bot Aktif!")


whil = False
free = 0

@bot.command("stream")
async def st(ctx):
    global whil, free
    if whil == True:
        whil = False
        free = 0
        tg_bot = Client("Tg", api_id=api_id, api_hash=api_hash, bot_token=tg)
        await tg_bot.start()
        await tg_bot.edit_message_text(chat_id=chat, message_id=message_id, text="**Sahibim şimdilik yayını kapattı!\n\nSanırım izlenmek istemiyor 👀**")
        await tg_bot.stop()
        return await ctx.send("```Durdurdum!```")
    whil = True
    free = 1
    await ctx.send("```Başlıyorum...```")
    current = ""
    while whil:
        if whil == False:
            return 
        user_activite = ctx.author.activities
        
        if len(user_activite) < 2:
            if free == 0:
                pass
            else:
                tg_bot = Client("Tg", api_id=api_id, api_hash=api_hash, bot_token=tg)
                await tg_bot.start()
                try:
                    await tg_bot.edit_message_text(chat_id=chat, message_id=message_id, text="**Şuan bir etkinlik gözükmüyor! Gelişme olduğunda haber veririm...**")
                except MessageNotModified:
                    pass
                await tg_bot.stop()
                free = 0
            
        else:
            if free == 0:
                free = 1
            user = user_activite
            text = ""
            n = 0
            for i in user:
                if n < 1:
                    n+=1
                else:
                    if str(i.type) == "ActivityType.playing":
                        try:
                            text += f"**[`{n}`]\nActivity: `Playing!`\n\n- Name: `{i.name}`\n\n- `{i.details}`**\n\n"
                        except AttributeError:
                            text += f"**[`{n}`]\nActivity: `Playing!`\n\n- Name: `{i.name}`\n**\n\n"
                    elif str(i.type) == "ActivityType.listening":
                        text += f"**[`{n}`]\nActivity: `Listening!`\n\n- Name: `{i.title}`\n\n- Artist: `{i.artist}`**\n\n"
                    n+=1
            if not text == current:
                tg_bot = Client("Tg", api_id=api_id, api_hash=api_hash, bot_token=tg)
                await tg_bot.start()
                try:
                    await tg_bot.edit_message_text(chat_id=chat, message_id=message_id, text=text)
                except MessageNotModified:
                    pass
                await tg_bot.stop()
                current=text
        await asyncio.sleep(3)


    

bot.run(TOKEN)
