from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.schema import ForeignKey

from app import base


class SearchUrl(base):
    __tablename__ = "search_url"

    search_url_id = Column(Integer, primary_key=True)
    base_url = Column(Integer, ForeignKey("base_urls.base_url_id"), nullable=False)
    api_key = Column(Integer, ForeignKey("api_keys.api_key_id"), nullable=False)
    departure_airport = Column(String(3), ForeignKey("airports.iata"), nullable=False)
    arrival_airport = Column(String(3), ForeignKey("airports.iata"), nullable=False)
    departure_date = Column(DATE, nullable=False)

class ApiKey(base):
    __tablename__ = "api_keys"

    api_key_id = Column(Integer, primary_key=True)
    api_key = Column(String(50), nullable=False)


class BaseUrl(base):
    __tablename__ = "base_urls"

    base_url_id = Column(Integer, primary_key=True)
    base_url = Column(String(50), nullable=False)