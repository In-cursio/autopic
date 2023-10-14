import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "6620972"))
API_HASH = environ.get("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
SESSION = environ.get("SESSION", "1BVtsOJcBu5lNBH1DrJe6dZXqPnywXQzepRTmUT4DhDzfI7iDwu8y46Ao46aqt2u_IUcWWWOiWWiLNLc2CfvqBCbF9tMdK6nfX4xnQm0I-XhhENN7al4eTgSLw294MpEN4Eb0uqx-KxmmRF3mWYD-53v4ju7dtm1lLVQ-ZvhxMhaD6zLO9Brn-qdttbOy-eUtWStoSXTHklz1p3-t62_pZ3HaO5flrOhg3wKMPvHKh7es_T__ojMI_gdx9EuES85sNKnV2vGX148orx5_2YhoNXhfGSu8OfXyR0wNhA8lhku5yW_OTMkv6g_5w8oWYb9diAJ5vhI2Hs-D0lvtiCfnrxeCa_kNI74=")
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

