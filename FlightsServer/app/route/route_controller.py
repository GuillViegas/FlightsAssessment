from app.airport.airport import Airport
from app.route.route import Route
from app import session
from app.utils import calcDistanceKm
from sqlalchemy.orm.exc import NoResultFound


class RouteController:
    @staticmethod
    def createRoutes():
        airports = session.query(Airport).all()
        routes = []

        while(len(airports) != 0):
            origin = airports[0]
            airports.remove(airports[0])

            for dest in airports:
                dist = calcDistanceKm(origin.geom, dest.geom)

                try:
                    session.query(Route).filter_by(origin=origin.iata, destination=dest.iata).one()
                except NoResultFound:
                    r1 = Route(origin=origin.iata, destination=dest.iata, distance=dist)
                    session.add(r1)
                    routes.append(r1)

                try:
                    session.query(Route).filter_by(origin=dest.iata, destination=origin.iata).one()
                except NoResultFound:
                    r2 = Route(origin=dest.iata, destination=origin.iata, distance=dist)
                    session.add(r2)
                    routes.append(r2)

        session.commit()

        return routes
