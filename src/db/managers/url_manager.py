from sqlalchemy.orm import Session

from db.models import ShortURL


class URLManager:
    def __init__(self, db: Session):
        self.db = db

    def get_by_original(self, original_url: str) -> ShortURL | None:
        return self.db.query(ShortURL).filter(ShortURL.original_url == original_url).first()

    def get_by_code(self, code: str) -> ShortURL | None:
        return self.db.query(ShortURL).filter(ShortURL.code == code).first()

    def create(self, original_url: str, code: str) -> ShortURL:
        row = ShortURL(original_url=original_url, code=code)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return row

    def increment_clicks(self, row: ShortURL):
        row.clicks += 1
        self.db.commit()
