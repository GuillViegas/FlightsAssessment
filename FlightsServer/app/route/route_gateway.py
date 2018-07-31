from flask import Blueprint
from flask import Response
import json
from route_controller import RouteController


route = Blueprint('route', __name__, url_prefix='/route')


@route.route('/getlongesttripkm', methods=['GET'])
def getLongestTripKM():
    routeController = RouteController()
    response = routeController.getLongestTripKM()

    return Response(json.dumps(response), mimetype='application/json')