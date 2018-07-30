from haversine import haversine
from app import session
from geoalchemy2 import functions


def calcDistanceKm(geom1, geom2):
    coord1 = ST_AsTuple(session.query(functions.ST_AsText(geom1)).one())
    coord2 = ST_AsTuple(session.query(functions.ST_AsText(geom2)).one())

    return haversine(coord1, coord2)

def ST_AsTuple(coord):
    coord = coord[0].split("(")[1]
    coord = (lon, lat) = coord[:-1].split()

    return coord