from flask import Blueprint, Response, request
import json
from trip_controller import TripController


trip = Blueprint('trip', __name__, url_prefix='/trip')


@trip.route('/longestflightduration', methods=['GET'])
def longestFlightDuration():
    tripController = TripController()
    response = tripController.longestFlightDuration()

    return Response(json.dumps(response), mimetype='application/json')

@trip.route('/dosearch', methods=['GET'])
def doSearch():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure_date = request.args.get('departure_date')
    departure_date = departure_date.split('T')[0]

    tripController = TripController()
    response = tripController.doSearch(origin=origin, destination=destination, departure_date=departure_date)

    return Response(json.dumps(response), mimetype='application/json')