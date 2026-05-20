import os
from pathlib import Path

BOT_TOKEN = os.getenv("BOT_TOKEN")

_chat_id = os.getenv("CHAT_ID")
CHAT_ID = int(_chat_id) if _chat_id else None

BASE_DIR = Path(__file__).resolve().parent

PENDING_FILE = BASE_DIR / "pending.json"
TOPICS_FILE = BASE_DIR / "topics.json"
DATABASE_FILE = BASE_DIR / "database.json"
REMINDERS_FILE = BASE_DIR / "reminders.json"

DOWNLOAD_DIR = BASE_DIR / "downloads"
COOKIES_FILE = BASE_DIR / "cookies.txt"

ASSETS_DIR = BASE_DIR / "assets"
TOPICS_IMAGE = ASSETS_DIR / "topics.jpg"
INFO_IMAGE = ASSETS_DIR / "info.jpg"
EXPORT_IMAGE = ASSETS_DIR / "export.jpg"

DOWNLOAD_DIR.mkdir(exist_ok=True)

DEFAULT_TOPICS = {
    "Спорт аккаунты": {"id": 2, "icon": "⚽"}
}

PRIORITIES = {
    "high": {"label": "🔥 High", "short": "High"},
    "normal": {"label": "⭐ Normal", "short": "Normal"},
    "later": {"label": "🧊 Later", "short": "Later"}
}

STATUSES = {
    "new": "🆕 New",
    "progress": "🟡 In Progress",
    "done": "✅ Done",
    "bad": "❌ Not Suitable"
}
