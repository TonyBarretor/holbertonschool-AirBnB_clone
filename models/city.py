#!/usr/bin/python3
"""
City module for AirBnB clone project.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for representing a city.
    """
    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        # Agrega cualquier otra lógica de inicialización aquí

    def set_custom_property(self, value):
        """Set a custom property."""
        self.custom_property = value

    def get_custom_property(self):
        """Get the value of the custom property."""
        return getattr(self, 'custom_property', None)


if __name__ == '__main__':
    my_city = City()
    print(my_city)
