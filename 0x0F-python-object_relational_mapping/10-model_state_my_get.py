#!/usr/bin/python3
"""
    A script that returns the state id from hbtn_0e_6_usa that contains
    the name passed as an argument
    Username, password, dbname and state will be passed as arguments
    to the script.
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # Extract the id of the name passed and print
    state = session.query(State) \
                   .filter(State.name == sys.argv[4]).one_or_none()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
