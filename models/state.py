#!/usr/bin/python3
"""
State module for AirBnB clone project.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""


if __name__ == '__main__':
    my_state = State()
    print(my_state)
