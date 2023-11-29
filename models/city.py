#!/usr/bin/python3
"""
City module for AirBnB clone project.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for representing a city.
    """
    def __init__(self):
        """Initialize City instance."""
        pass


if __name__ == '__main__':
    my_city = City()
    print(my_city)
