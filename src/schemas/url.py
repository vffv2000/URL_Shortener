from datetime import datetime
from pydantic import BaseModel, HttpUrl


class ShortenIn(BaseModel):
    """
    Input schema for shortening a URL.

    Attributes:
        url (HttpUrl): The original URL to be shortened. Validates proper HTTP/HTTPS format.
    """
    url: HttpUrl


class ShortenOut(BaseModel):
    """
    Output schema for the shortened URL.

    Attributes:
        code (str): The unique code representing the shortened URL.
        short_url (str): The full shortened URL including the base URL.
    """
    code: str
    short_url: str


class StatsOut(BaseModel):
    """
    Output schema for URL statistics.

    Attributes:
        code (str): The unique code representing the shortened URL.
        original_url (str): The original URL.
        clicks (int): Number of times the shortened URL has been accessed.
        created_at (datetime): Timestamp when the URL was shortened.
    """
    code: str
    original_url: str
    clicks: int
    created_at: datetime
