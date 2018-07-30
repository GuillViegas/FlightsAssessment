from sqlalchemy import Column, String, Integer
from app import base


class BaseUrl(base):
    __tablename__ = "base_urls"

    base_url_id = Column(Integer, primary_key=True)
    base_url = Column(String(50), nullable=False)
