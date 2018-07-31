from flask import Blueprint
from flask import Response
import json
from trip_controller import TripController


trip = Blueprint('trip', __name__, url_prefix='/trip')


@trip.route('/longestflightduration', methods=['GET'])
def longestFlightDuration():
    tripController = TripController()
    response = tripController.longestFlightDuration()

    return Response(json.dumps(response), mimetype='application/json')
