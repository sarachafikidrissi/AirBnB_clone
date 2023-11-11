#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestStateInstantiation(unittest.TestCase):
    """Unittests for State class instantiation."""

    def test_instantiation(self):
        """Test that an instance of State is correctly created without any arguments."""
        self.assertEqual(State, type(State()))

    def test_stored_in_objects(self):
        """Test that a new instance of State is stored in the objects dictionary."""
        self.assertIn(State(), models.storage.all().values())

    def test_id_type(self):
        """Test that the 'id' attribute of State is of type string."""
        self.assertEqual(str, type(State().id))

    def test_created_at_type(self):
        """Test that the 'created_at' attribute of State is of type datetime."""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_type(self):
        """Test that the 'updated_at' attribute of State is of type datetime."""
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_ATTR(self):
        """Test that 'name' is a public class attribute of State."""
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_unique_ids(self):
        """Test that two states have unique IDs."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_created_at(self):
        """Test that two states have different 'created_at' timestamps."""
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_different_updated_at(self):
        """Test that two states have different 'updated_at' timestamps."""
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a State object."""
        dt = datetime.today()
        dt_repr = repr(dt)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + dt_repr, state_str)
        self.assertIn("'updated_at': " + dt_repr, state_str)

    def test_args_unused(self):
        """Test instantiation of State with unused arguments."""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of State with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of State with None keyword arguments."""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()

