#!/usr/bin/python3
"""
Amenity module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""


if __name__ == '__main__':
    my_amenity = Amenity()
    print(my_amenity)
