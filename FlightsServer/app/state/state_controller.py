from app.state.state import State
from app import session, db


class StateController:
    def getStateMostNumberOfAirports(self):
        sql = '''SELECT state, COUNT(state) number_airports 
                 FROM airports 
                 GROUP BY state 
                 ORDER BY number_airports DESC 
                 LIMIT 1'''

        states = db.execute(sql)

        for state in states:
            state = session.query(State).filter_by(state_id=state[0]).one()

        return { 'name': state.name,
                 'region': state.region,
                 'cod': state.cod }
