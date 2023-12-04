#!/usr/bin/python3
"""
Review module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""


if __name__ == '__main__':
    my_review = Review()
    print(my_review)
