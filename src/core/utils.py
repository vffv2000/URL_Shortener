import secrets
import string

from core.config import settings

_ALPHABET = string.ascii_letters + string.digits  # a-zA-Z0-9


def generate_code(length: int = settings.code_length) -> str:
    return "".join(secrets.choice(_ALPHABET) for _ in range(length))