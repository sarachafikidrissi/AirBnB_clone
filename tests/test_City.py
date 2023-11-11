#!/usr/bin/python3
"""Defines unittests for models/city.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCityInstantiation(unittest.TestCase):
    """Unittests for City class instantiation with different arguments."""

    def test_no_args_instantiates(self):
        """Test that creating a City instance with no arguments results in an instance of City."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that a newly created City instance is stored in the objects dictionary."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of a City instance is a string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test that the 'created_at' attribute of a City instance is of type datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the 'updated_at' attribute of a City instance is of type datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """Test that 'state_id' is a public class attribute of the City class."""
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test that 'name' is a public class attribute of the City class."""
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))

    def test_two_cities_unique_ids(self):
        """Test that two City instances have unique IDs."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_cities_different_created_at(self):
        """Test that two City instances have different 'created_at' timestamps."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test that two City instances have different 'updated_at' timestamps."""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a City instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + dt_repr, city_str)
        self.assertIn("'updated_at': " + dt_repr, city_str)

    def test_args_unused(self):
        """Test that passing None as an argument to City does not set any instance attributes to None."""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of City with keyword arguments (kwargs)."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test that passing None as kwargs raises a TypeError."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
