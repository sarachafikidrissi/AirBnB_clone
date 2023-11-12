#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_instantiation_without_arguments(self):
        """Test that an instance of the Place class can be created without
        passing any arguments. It checks the type of the created instance and
        its 'id' and 'created_at' attributes.
        """
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test that a newly created instance of Place is stored in the
        'objects' dictionary in models.storage.
        """
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of a Place instance is of type str."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test that the 'created_at' attribute of a Place instance is of type
        datetime.
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the 'updated_at' attribute of a Place instance is of type
        datetime.
        """
        self.assertEqual(datetime, type(Place().updated_at))


if __name__ == "__main__":
    unittest.main()
