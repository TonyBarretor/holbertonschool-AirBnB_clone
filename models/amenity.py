#!/usr/bin/python3
"""
Amenity module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing an amenity.
    """
    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        # Add any other initialization logic here
        self.set_custom_property(None)  # Default value for custom_property

    def set_custom_property(self, value):
        """Set a custom property."""
        self.custom_property = value

    def get_custom_property(self):
        """Get the value of the custom property."""
        return getattr(self, 'custom_property', None)


if __name__ == '__main__':
    my_amenity = Amenity()
    print(my_amenity)
