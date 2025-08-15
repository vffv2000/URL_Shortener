from fastapi import HTTPException

from core.utils import generate_code
from db.managers.url_manager import URLManager


class URLService:
    """
    Service layer for URL shortening operations.

    Handles URL shortening, retrieval, redirection, and statistics.
    """

    def __init__(self, manager: URLManager):
        """
        Initialize the URL service with a URL manager.

        Args:
            manager (URLManager): Database manager for ShortURL operations.
        """
        self.manager = manager

    def shorten_url(self, original_url: str) -> str:
        """
        Shorten a given original URL. If the URL already exists, return its code.

        Generates a unique code for new URLs and saves it in the database.

        Args:
            original_url (str): The URL to shorten.

        Returns:
            str: The unique code representing the shortened URL.

        Raises:
            HTTPException: If a unique code cannot be generated after 10 attempts.
        """
        existing = self.manager.get_by_original(original_url)
        if existing:
            return existing.code

        for _ in range(10):
            code = generate_code(6)
            if not self.manager.get_by_code(code):
                break
        else:
            raise HTTPException(status_code=500, detail="Failed to generate unique code")

        row = self.manager.create(original_url, code)
        return row.code

    def get_redirect_url(self, code: str) -> str:
        """
        Retrieve the original URL by its shortened code and increment click count.

        Args:
            code (str): The code of the shortened URL.

        Returns:
            str: The original URL to redirect to.

        Raises:
            HTTPException: If the code is not found in the database.
        """
        row = self.manager.get_by_code(code)
        if not row:
            raise HTTPException(status_code=404, detail="Code not found")
        self.manager.increment_clicks(row)
        return row.original_url

    def get_stats(self, code: str):
        """
        Retrieve statistics for a given shortened URL code.

        Args:
            code (str): The code of the shortened URL.

        Returns:
            ShortURL: The database row containing original URL, clicks, and creation timestamp.

        Raises:
            HTTPException: If the code is not found in the database.
        """
        row = self.manager.get_by_code(code)
        if not row:
            raise HTTPException(status_code=404, detail="Code not found")
        return row
