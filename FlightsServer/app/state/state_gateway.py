from flask import Blueprint
from flask import Response
import json
from state_controller import StateController


state = Blueprint('state', __name__, url_prefix='/state')


@state.route('/getstatemostnumberairports', methods=['GET'])
def getStateMostNumberOfAirports():
    stateController = StateController()
    response = stateController.getStateMostNumberOfAirports()

    return Response(json.dumps(response), mimetype='application/json')