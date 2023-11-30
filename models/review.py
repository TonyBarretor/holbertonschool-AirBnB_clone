#!/usr/bin/python3
"""
Review module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing a review.
    """
    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        # Add any other initialization logic here

    def set_custom_rating(self, rating):
        """Set a custom rating."""
        self.custom_rating = rating

    def get_custom_rating(self):
        """Get the value of the custom rating."""
        return getattr(self, 'custom_rating', None)


if __name__ == '__main__':
    my_review = Review()
    print(my_review)
