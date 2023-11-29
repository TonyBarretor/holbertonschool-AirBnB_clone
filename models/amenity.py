#!/usr/bin/python3
"""
Amenity module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing an amenity.
    """
    def __init__(self):
        """Initialize Amenity instance."""
        pass


if __name__ == '__main__':
    my_amenity = Amenity()
    print(my_amenity)
