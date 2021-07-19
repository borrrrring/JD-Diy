from .. import chat_id, jdbot, logger, chname, mybot
from ..bot.utils import  V4, QL
from telethon import events
import os


@jdbot.on(events.NewMessage(from_users=chat_id, pattern=r'^/restart$'))
async def myrestart(event):
    try:
        if V4:
            await jdbot.send_message(chat_id, "重启程序")
            os.system("pm2 restart jbot")
        elif QL:
            await jdbot.send_message(chat_id, "重启程序")
            os.system("ql bot")
    except Exception as e:
        await jdbot.send_message(chat_id, 'something wrong,I\'m sorry\n' + str(e))
        logger.error('something wrong,I\'m sorry\n' + str(e))


if chname:
    jdbot.add_event_handler(myrestart, events.NewMessage(from_users=chat_id, pattern=mybot['命令别名']['cron']))

