from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Index

Base = declarative_base()


class ShortURL(Base):
    """
    SQLAlchemy model representing a shortened URL record.

    Attributes:
        id (int): Primary key of the record.
        original_url (str): The original full URL.
        code (str): Unique short code for the URL.
        clicks (int): Number of times the short URL has been accessed.
        created_at (datetime): Timestamp when the record was created.
    """

    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(2048), nullable=False, index=True)
    code = Column(String(16), nullable=False, unique=True, index=True)
    clicks = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        Index("ix_short_urls_code", "code", unique=True),
    )
