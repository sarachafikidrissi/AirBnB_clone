#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityAttributes(unittest.TestCase):
    """Unittests for Amenity class attributes."""

    def test_instantiation(self):
        """Test Amenity is correctly created without any arguments."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_stored_in_objects(self):
        """Test Amenity is stored in the objects dictionary."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_type(self):
        """Test that the 'id' attribute of Amenity is of type string."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_type(self):
        """Test'created_at' attribute of Amenity is of type datetime."""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_type(self):
        """Test'updated_at' attribute of Amenity is of type datetime."""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_ATTR(self):
        """Test that 'name' is a public class attribute of Amenity."""
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(amenity))
        self.assertNotIn("name", amenity.__dict__)

    def test_unique_ids(self):
        """Test that two instances of Amenity have unique IDs."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_different_created_at(self):
        """Test two instances have different 'created_at' timestamps."""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_different_updated_at(self):
        """Test two instances have different 'updated_at' timestamps."""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        """Test the string representation of an Amenity instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + dt_repr, amenity_str)
        self.assertIn("'updated_at': " + dt_repr, amenity_str)

    def test_args_unused(self):
        """Test with None as argument results in no None values in __dict__."""
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of Amenity with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test with None as keyword arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
