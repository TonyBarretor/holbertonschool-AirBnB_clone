#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for representing the base model.
    """
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()


if __name__ == '__main__':
    my_model = BaseModel()
    print(my_model)
