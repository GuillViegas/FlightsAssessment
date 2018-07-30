from app import session, db
from app.aircraft.aircraft import Aircraft, Manufacturer
from sqlalchemy.orm.exc import NoResultFound


class AircraftController:
    def searchForAircraft(self, aircraft, manufacturer):
        try:
            aircraftdb = session.query(Aircraft).filter_by(name=aircraft).one()
        except NoResultFound:
            try:
                manufacturerdb = session.query(Manufacturer).filter_by(name=manufacturer).one()
            except NoResultFound:
                manufacturerdb = Manufacturer(name=manufacturer)
                session.add(manufacturerdb)
                session.commit()
                session.refresh(manufacturerdb)

            aircraftdb = Aircraft(name=aircraft, manufacturer=manufacturerdb.manufacturer_id)
            session.add(aircraftdb)
            session.commit()
            session.refresh(aircraftdb)

        return aircraftdb

    def setAllAircraftSpeed(self):
        sql = '''SELECT a.aircraft_id, SUM(r.distance), SUM(t.duration) FROM routes r, trips t, aircrafts a WHERE
                        t.aircraft = a.aircraft_id AND t.route = r.route_id GROUP BY a.aircraft_id'''
        aircrafts_speed = db.execute(sql)

        for aircraft in aircrafts_speed:
            speed = aircraft[1] / float(aircraft[2].total_seconds()) * 3600
            session.query(Aircraft).filter(Aircraft.aircraft_id == aircraft[0]).update({'speed': speed})

        session.commit()

    def setAllAircraftPriceKM(self):
        sql = '''SELECT a.aircraft_id, SUM(r.distance), SUM(t.price) FROM routes r, trips t, aircrafts a WHERE
                                t.aircraft = a.aircraft_id AND t.route = r.route_id GROUP BY a.aircraft_id'''

        aircrafts_speed = db.execute(sql)

        for aircraft in aircrafts_speed:
            price_km = float(aircraft[2])/aircraft[1]
            session.query(Aircraft).filter(Aircraft.aircraft_id == aircraft[0]).update({'price_km': price_km})

        session.commit()