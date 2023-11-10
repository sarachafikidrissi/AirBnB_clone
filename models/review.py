#!/usr/bin/python3
"""This is review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from BaseModel

    Attributes:
        place_id (str): public class attribute for Review's place_id
        user_id (str): public class attribute for Review's user_id
        text (str): public class attribute for Review's text
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor method for Review class

        Attributes:
            args (list):  argument in a list form
            kwargs (dict): argument in a dictionnary form
        """
        super().__init__(*args, **kwargs)
