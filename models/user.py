#!/usr/bin/python3
"""
Place module for AirBnB clone project.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for representing a user.
    """
    def __init__(self):
        """Initialize User instance."""
        super().__init__()
        self.friends = []

    def add_friend(self, friend_name):
        """Add a friend to the user."""
        self.friends.append(friend_name)


if __name__ == '__main__':
    my_user = User()
    print(my_user)
