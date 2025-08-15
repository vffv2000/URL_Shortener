from sqlalchemy.orm import Session

from db.models import ShortURL


class URLManager:
    """
    Manager class for interacting with ShortURL records in the database.

    Provides methods to retrieve, create, and update ShortURL entries.
    """

    def __init__(self, db: Session):
        """
        Initialize the URLManager with a database session.

        Args:
            db (Session): SQLAlchemy database session.
        """
        self.db = db

    def get_by_original(self, original_url: str) -> ShortURL | None:
        """
        Retrieve a ShortURL record by its original URL.

        Args:
            original_url (str): The original URL to search for.

        Returns:
            ShortURL | None: The matching ShortURL record, or None if not found.
        """
        return self.db.query(ShortURL).filter(ShortURL.original_url == original_url).first()

    def get_by_code(self, code: str) -> ShortURL | None:
        """
        Retrieve a ShortURL record by its short code.

        Args:
            code (str): The short code associated with the URL.

        Returns:
            ShortURL | None: The matching ShortURL record, or None if not found.
        """
        return self.db.query(ShortURL).filter(ShortURL.code == code).first()

    def create(self, original_url: str, code: str) -> ShortURL:
        """
        Create a new ShortURL record in the database.

        Args:
            original_url (str): The original URL to shorten.
            code (str): The unique short code for the URL.

        Returns:
            ShortURL: The newly created ShortURL record.
        """
        row = ShortURL(original_url=original_url, code=code)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return row

    def increment_clicks(self, row: ShortURL):
        """
        Increment the click counter of a ShortURL record.

        Args:
            row (ShortURL): The ShortURL record to update.
        """
        row.clicks += 1
        self.db.commit()
