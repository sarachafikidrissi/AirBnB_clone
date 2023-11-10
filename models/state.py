#!/usr/bin/python3
"""This is state Module that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class
    Attribute:
       name : public classe attribute for name state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
