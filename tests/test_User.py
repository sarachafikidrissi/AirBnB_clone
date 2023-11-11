#!/usr/bin/python3
"""Defines unittests for models/user.py.

"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserClass(unittest.TestCase):
    """Unittests for testing the User class."""

    def test_NoArgs_instantiates(self):
	"""Test that an instance of user is created without passing any arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
	"""Test that a new instance of user is stored in the objects dictionary."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
	"""Test that the 'id' attribute of user is a string."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
	""" test that created at is a datetime"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
	""" test that update at is datetime """
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_attribute_is_a_string(self):
        """Test that the 'email' attribute of User is a string."""
        self.assertEqual(str, type(User.email))

    def test_password_attribute_is_a_string(self):
        """Test that the 'password' attribute of User is a string."""
        self.assertEqual(str, type(User.password))

    def test_first_name_attribute_is_a_string(self):
        """Test that the 'first_name' attribute of User is a string."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_attribute_is_a_string(self):
        """Test that the 'last_name' attribute of User is a string."""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_have_unique_ids(self):
        """Test that two instances of User have different 'id' values."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_have_different_created_at(self):
        """Test that two instances of User have different 'created_at' timestamps."""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_have_different_updated_at(self):
        """Test that two instances of User have different 'updated_at' timestamps."""
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation_includes_id_and_timestamps(self):
        """Test that the __str__ representation of User includes 'id', 'created_at', and 'updated_at'."""
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)


    def test_unused_args_are_ignored(self):
        """Test that unused arguments passed to the constructor are ignored."""
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_keyword_arguments(self):
        """Test that User can be instantiated with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_keyword_arguments_raises_type_error(self):
        """Test that attempting to instantiate User with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)
          


if __name__ == "__main__":
    unittest.main()
