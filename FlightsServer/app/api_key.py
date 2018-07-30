from sqlalchemy import Column, String, Integer
from app import base


class ApiKey(base):
    __tablename__ = "api_keys"

    api_key_id = Column(Integer, primary_key=True)
    api_key = Column(String(50), nullable=False)