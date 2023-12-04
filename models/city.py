#!/usr/bin/python3
"""
City module for AirBnB clone project.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""


if __name__ == '__main__':
    my_city = City()
    print(my_city)
