import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "29922662"))
API_HASH = environ.get("API_HASH", "fabd9f89368de7cc31357522a0089a56")
SESSION = environ.get("SESSION", "1BVtsOGcBu02XzTBBB3h0UpHpmBx-Q7JiBi3Gv1QZfoGz1jXmTOxISsxMCsAI_F6i9i0fyN7azqX-5zZtawGYm43PvkKqVm05lCfMzZu9xG-yAfVKv88oKvqB6kAAiBjT7WZW5A4l4Y4OW8aM9_b0KZFyCkZ5u8rcpeZbZILwnes9A3lNmE6j_JDd8WZHT8WaN5rLaLTlpQXa9KyNYmG4VWztY51xaDprDUp5GeC2toR2QJmpiMo9qW-H1Ecl9cN4mVCNgvuj5siSeWpevs1Z_3os7Grx6Ihn8GCNE-Qyd-rX_jQ3MyWQquP-6X8PyiD33UCx0R2FOsq0ROb6O-cNlXqYk-EQvMY=")
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

