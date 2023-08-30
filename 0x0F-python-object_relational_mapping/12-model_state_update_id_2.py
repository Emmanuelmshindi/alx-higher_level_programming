#!/usr/bin/python3
"""
    A script that updates State at id=2 to New Mexico
    Username, password, dbname will be passed as arguments to the script.
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

    state_update = session.query(State).get(2)

    state_update.name = 'New Mexico'

    session.add(state_update)

    session.commit()
    state.close()
