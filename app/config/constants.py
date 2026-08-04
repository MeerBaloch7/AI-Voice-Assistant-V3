from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

APP_DIR = PROJECT_ROOT / "app"

DATA_DIR = PROJECT_ROOT / "data"

LOG_DIR = PROJECT_ROOT / "logs"

CACHE_DIR = DATA_DIR / "cache"

MODEL_DIR = DATA_DIR / "models"

DEFAULT_TIMEOUT = 30

MAX_CONVERSATION_HISTORY = 20

APP_VERSION = "3.0.0"
DEFAULT_EPISODE_IMPORTANCE = 1
