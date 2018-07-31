from config import BASE_URL, API_KEY_2XT
from search_url import BaseUrl, ApiKey, SearchUrl
from sqlalchemy.orm.exc import NoResultFound
from app import session


class SearchUrlController:
    def postSearchUrl(self, departure_airport, arrival_airport,
                              departure_date, base_url=BASE_URL, api_key=API_KEY_2XT):

        try:
            baseUrl = session.query(BaseUrl).filter_by(base_url=base_url.strip()).one()

        except NoResultFound:
            baseUrl = BaseUrl(base_url=base_url)
            session.add(baseUrl)
            session.commit()

        try:
            apiKey = session.query(ApiKey).filter_by(api_key=api_key).one()

        except NoResultFound:
            apiKey = ApiKey(api_key=api_key)
            session.add(apiKey)
            session.commit()

        searchUrl = SearchUrl(base_url=baseUrl.base_url_id, api_key=apiKey.api_key_id, departure_airport=departure_airport,
                  arrival_airport=arrival_airport, departure_date=departure_date)
        session.add(searchUrl)
        session.commit()

        return searchUrl
