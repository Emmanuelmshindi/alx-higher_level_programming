#!/usr/bin/python3
"""
    A script that adds a state object Louisiana
    to the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                       sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

# Create a session
session = Session()

# Add state
state = State(name="Louisiana")

session.add(state)

session.commit()

print(state.id)

session.close()
