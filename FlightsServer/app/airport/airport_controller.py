import requests
from airport import Airport
from app.city.city import City
from app.state.state import State
from config import CREDENCIAL_2XT, API_KEY_2XT
from app import session, db
from sqlalchemy.orm.exc import NoResultFound


class AirportController:
    @staticmethod
    def getAirportsFromUrl():
        r = requests.get('http://stub.2xt.com.br/air/airports/%s' % API_KEY_2XT, auth=CREDENCIAL_2XT)
        airports = r.json()

        return airports

    def storeAirpotsDB(self):
        airports_list = []
        airports = self.getAirportsFromUrl()

        for airport in airports:
            iata = airports[airport]['iata']

            try:
                session.query(Airport).filter_by(iata=iata).one()
            except NoResultFound:
                city_name = airports[airport]['city']

                try:
                    city = session.query(City).filter_by(name=city_name).one()
                except NoResultFound:
                    try:
                        state_cod = airports[airport]['state'].strip()
                        try:
                            state = session.query(State).filter_by(cod=state_cod).one()
                        except NoResultFound:
                            raise ValueError('State does not match any record in the database!')

                    except Exception as error:
                        print('Error: ' + repr(error))
                        return 0

                    else:
                        city = City(name=city_name, state_id=state.state_id)
                        session.add(city)
                        session.commit()

                coord = "SRID=4674;POINT(%s %s)" % (airports[airport]["lat"], airports[airport]["lon"])
                airport = Airport(iata=iata, city=city.city_id, geom=coord)
                airports_list.append(airport)
                session.add(airport)
                session.commit()

        return airports_list

    def getAiportStatistics(self):
        sql = '''SELECT q1.origin, q1.destination, q1.minn, q2.destination, q2.maxx FROM

                           (SELECT r.origin origin, r.destination destination, q.min minn FROM

                            (	SELECT origin, min(distance)
                               FROM routes
                                GROUP BY origin ) q

                           JOIN routes r ON r.origin = q.origin AND q.min = r.distance) q1

                            JOIN

                            (SELECT r.origin origin, r.destination destination, q.max maxx FROM

                            (	SELECT origin, max(distance)
                                FROM routes
                                GROUP BY origin ) q

                            JOIN routes r ON r.origin = q.origin AND q.max = r.distance) q2 ON q1.origin = q2.origin;'''

        statistics = db.execute(sql)
        airportStatistics = []

        for statistic in statistics:
            airportStatistics.append({'origin': statistic[0], 'nearest': statistic[1], 'min_distance': statistic[2], 'farthest': statistic[3], 'max_distance': statistic[4]})

        return airportStatistics
