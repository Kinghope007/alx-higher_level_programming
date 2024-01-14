#!/usr/bin/python3
"""
Script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query State objects containing the letter 'a' and print the results
    states_with_a = sesion.query(State).order_by(State.id)
    for state in states_with_a:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()
