import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "6620972"))
API_HASH = environ.get("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
SESSION = environ.get("SESSION", "BQCxw1pNin5BLpgc22AQpWdQlINVqBN93Oenoe7w8i00GUWd7_PVjvuo5TaHlFoA5gICVHX9UfMKEfNkKeaDIjVnOqyqOzkv_TWzBLcivQMWR8-jTb9bM5yFy5ahD1OtaXsBsKwIUN-OTJulsUIJu1-tmbtge2-voAIjolbky_q8mvS2kYOJSP_9luUU0GUn52wX9h8BNm4WxPL-iVlq7j1YPUu5sQCZT0MhnxgQOp2HsLXeJiWyGfn7lszYhZSktoB3rpFCGZufHuoGFYbW8pxavyCx_lEK4R463Di8HhFqPtZ628CfDwxRYgK04miv8liF5_ShpOHkp6QgAk7X_lTBaANPBgA")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001836315219"))


if SESSION is not None:
    session = StringSession(str(SESSION))
else:
    session = "pyrobot"

try:
    client = TelegramClient(
        session=session,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )
    client.start()
    
except Exception as e:
    print(e)

