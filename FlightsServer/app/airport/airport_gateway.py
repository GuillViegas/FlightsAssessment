from flask import Blueprint
from flask import Response
import json
from airport_controller import AirportController


airport = Blueprint('airport', __name__, url_prefix='/airport')


@airport.route('/getairportstatistics', methods=['GET'])
def getAiportStatistics():
    airportController = AirportController()
    response = airportController.getAiportStatistics()

    return Response(json.dumps(response), mimetype='application/json')
