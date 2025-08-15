from fastapi import HTTPException

from core.utils import generate_code
from db.managers.url_manager import URLManager


class URLService:
    def __init__(self, manager: URLManager):
        self.manager = manager

    def shorten_url(self, original_url: str) -> str:
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
        row = self.manager.get_by_code(code)
        if not row:
            raise HTTPException(status_code=404, detail="Code not found")
        self.manager.increment_clicks(row)
        return row.original_url

    def get_stats(self, code: str):
        row = self.manager.get_by_code(code)
        if not row:
            raise HTTPException(status_code=404, detail="Code not found")
        return row
