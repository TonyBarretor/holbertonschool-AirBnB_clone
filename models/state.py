#!/usr/bin/python3
"""
State module for AirBnB clone project.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for representing a state.
    """
    def __init__(self):
        """Initialize State instance."""
        super().__init__()
        self.capital = ""


if __name__ == '__main__':
    my_state = State()
    print(my_state)
