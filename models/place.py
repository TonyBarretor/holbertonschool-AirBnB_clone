#!/usr/bin/python3
"""
Place module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for representing a place.
    """
    def __init__(self):
        """Initialize Place instance."""
        pass


if __name__ == '__main__':
    my_place = Place()
    print(my_place)
