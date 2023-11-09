#!/usr/bin/python3
"""This is base_model Module
This module defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the BaseModule Class
    """

    def __init__(self, *args, **kwargs):
        """constructor Method for BaseModel

        Args:
            args : argument constructor
            kwargs: argument constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'
                    )
                elif key == 'id':
                    self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A formatted string with class name, object ID,
            and object attributes.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
