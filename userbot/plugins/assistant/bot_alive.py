from telethon import events

from userbot import ALIVE_NAME, bot
from userbot.plugins import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/24fd20728dc7bc7a6155c.jpg"
pm_caption = " **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += " **SYSTEMS STATS**\n"
pm_caption += " **Telethon Version:** `1.15.0` \n"
pm_caption += " **Python:** `3.7.4` \n"
pm_caption += " **Database Status:**  `Functional`\n"
pm_caption += " **Current Branch** : `master`\n"
pm_caption += f" **Version** : `{currentversion}`\n"
pm_caption += f" **My Boss** : {DEFAULTUSER} \n"
pm_caption += " **License** : [GNU General Public License v3.0](github.com/PerU-MoNsteR/Eliza/blob/master/LICENSE)\n"
pm_caption += " **Copyright** : By [JARVIS WORKS](GitHub.com/PerU-MoNsteR)\n"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def jarvis(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)