from .logger import Logger
from base64 import b64decode

log = Logger()


def get_userId_from_token(token: str) -> int:
    bot_id_encoded = token.split(".")[0]
    missing_padding = len(bot_id_encoded) % 4
    if missing_padding:
        bot_id_encoded += "=" * (4 - missing_padding)
    return int(b64decode(bot_id_encoded).decode("utf-8"))