#!/usr/bin/python3
"""Defines unittests for models/review.py.

"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class TestReviewInstantiation(unittest.TestCase):
    """Unittests for Review class instantiation."""

    def test_instantiation(self):
        """Test that an instance of Review is correctly created without any arguments."""
        self.assertEqual(Review, type(Review()))

    def test_stored_in_objects(self):
        """Test that a new instance of Review is stored in the objects dictionary."""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_type(self):
        """Test that the 'id' attribute of Review is of type string."""
        self.assertEqual(str, type(Review().id))

    def test_created_at_type(self):
        """Test that the 'created_at' attribute of Review is of type datetime."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_type(self):
        """Test that the 'updated_at' attribute of Review is of type datetime."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_ATTR(self):
        """Test that 'place_id' is a public class attribute of Review."""
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id_ATTR(self):
        """Test that 'user_id' is a public class attribute of Review."""
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_ATTR(self):
        """Test that 'text' is a public class attribute of Review."""
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_unique_ids(self):
        """Test that two reviews have unique IDs."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_different_created_at(self):
        """Test that two reviews have different 'created_at' timestamps."""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_different_updated_at(self):
        """Test that two reviews have different 'updated_at' timestamps."""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a Review object."""
        dt = datetime.today()
        dt_repr = repr(dt)
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = dt
        review_str = review.__str__()
        self.assertIn("[Review] (123456)", review_str)
        self.assertIn("'id': '123456'", review_str)
        self.assertIn("'created_at': " + dt_repr, review_str)
        self.assertIn("'updated_at': " + dt_repr, review_str)	

    def test_args_unused(self):
        """Test that Review instantiation with None does not include None in the object's attributes."""
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test that Review can be instantiated with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test that Review instantiation with None keyword arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
