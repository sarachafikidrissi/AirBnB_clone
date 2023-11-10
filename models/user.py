#!/usr/bin/python3
"""This is user Module that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A Class that inherits from BaseModel

    Attributes:
        email (str): Public class attribute for email's User
        password (str): Public class attribute for password's User
        first_name (str): Public class attribute for first name's User
        last_name (str): Public class attribute for last name's User
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """init method for User class

        Attributes:
            args (list): argument in a list form
            kwargs (dict): argument in a dictionnary form
        """
        super().__init__(*args, **kwargs)
