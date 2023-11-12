#!/usr/bin/python3
"""Defines unittests for models/user.py.

"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """
    Unit tests for testing the instantiation of the User class.
    """

    def test_instantiation_with_no_arguments(self):
        """
        Test that a User instance can be created with no arguments.
        """
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new User instance is stored in the objects dictionary.
        """
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
        Test that the 'id' attribute of a User instance is a string.
        """
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """
        Test 'created_at' attribute of a User instance is a datetime object.
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test 'updated_at' attribute of a User instance is a datetime object.
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """
        Test that the 'email' attribute of the User class is a string.
        """
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """
        Test that the 'password' attribute of the User class is a string.
        """
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """
        Test that the 'first_name' attribute of the User class is a string.
        """
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """
        Test that the 'last_name' attribute of the User class is a string.
        """
        self.assertEqual(str, type(User.last_name))

    def test_two_users_have_unique_ids(self):
        """
        Test that two User instances have unique 'id' values.
        """
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_have_different_created_at(self):
        """
        Test that two User instances have different 'created_at' timestamps.
        """
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_have_different_updated_at(self):
        """
        Test that two User instances have different 'updated_at' timestamps.
        """
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of a User instance.
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)


if __name__ == "__main__":
    unittest.main()
