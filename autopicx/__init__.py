import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "6620972"))
API_HASH = environ.get("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
SESSION = environ.get("SESSION", "1BVtsOHMBu8J0iTkcf-xSm7pCHbtaEsOG44KBFxp3tLlgaZb_drfOytoJpJ3bivRzPT0OKqqBJiTXtSj9sxNztZBWjE4VwBXfBCfsMXfmi9xYdW37roZ1xo1AdfsfmYZ5q4JCVaw4TDg42TWi8caxgY9zIc-c9fHe1mDFsnhelJWkkscP6gUQZK8ROpIWB8ZK5rDLS-HsGk3muMwjYB2wpfKAeAUphV-1YTE6AEmmyuCSAwwpjV8_QSNUasRC5lGqD_nE8ZGmdFPCb84t8IpGzCBvCLpecNgritCUoL28ouC7iHWrcEUUk6QDJrekpC6Rd4zelzNuPlO2zFA6wJFHeELv6w_S_t0=")
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

