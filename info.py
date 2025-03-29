# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "10412514")
API_HASH = environ.get("API_HASH" , "4d55a7064ad72adcfa8944f505453a8c")
BOT_TOKEN = environ.get("BOT_TOKEN" , "7666348795:AAFl-JKS7sqxJjcVYrIbI4oWMDy6yjsckSA")
ADMIN = int(environ.get("ADMIN" , "1065743814"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-100"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002454478302")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://Dsrpdf2k25:Dsrpdf2k25@cluster0.wmt2w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1001734958816")
)
FSUB = environ.get("FSUB", False)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
