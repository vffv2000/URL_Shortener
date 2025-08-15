import secrets
import string

from core.config import settings

_ALPHABET = string.ascii_letters + string.digits  # a-zA-Z0-9


def generate_code(length: int = settings.code_length) -> str:
    """
    Generate a random alphanumeric code.

    The code consists of uppercase letters, lowercase letters, and digits.
    Uses `secrets.choice` for cryptographically secure random generation.

    Args:
        length (int, optional): Length of the generated code.
            Defaults to `settings.code_length`.

    Returns:
        str: Randomly generated alphanumeric code.
    """
    return "".join(secrets.choice(_ALPHABET) for _ in range(length))