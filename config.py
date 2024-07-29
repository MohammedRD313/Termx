from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 23970174))
API_HASH = getenv("API_HASH","f1db2e38b2c73448ef09c504187e888d")

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Hamodey2006:Hamodey2006@cluster0.xilnp5n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 5488301592))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/YY7365923851:AAGlgzoywP0I1imV97WN7eEdkCt6_imWi_E5Y8")
