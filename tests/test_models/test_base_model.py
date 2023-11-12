#!/usr/bin/python3
"""This is test_base_model
provides testing methods
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import inspect
from contextlib import redirect_stdout


class TestBaseModel(unittest.TestCase):
    """This is a Class for testing BaseModel class methods
    """

    @classmethod
    def setUpClass(cls):
        """Method that test doc
        """
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        """ setup method for the object 'obj' of BaseModel
        """
        self.obj = BaseModel()

    def tearDown(self):
        """teardown method for the object 'obj' of BaseModel
        """
        self.obj = None

    def test_module_docstring(self):
        """checks the existence of Docstring documentation
        in modules
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """checks the existence of Docstring documentation
        in class
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        checks the existence of Docstring documentation
        in modules
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_type(self):
        """test for class instance type
        """
        self.assertIsInstance(self.obj, BaseModel)
        self.assertEqual(type(self.obj), BaseModel)

    def test_default_attributes(self):
        """test for default attribues
        """
        self.assertIsNotNone(self.obj.id)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertEqual(self.obj.created_at, self.obj.updated_at)

    def test_basic_attributes(self):
        """test for basic attributes
        """
        self.obj.first_name = 'sara'
        self.obj.last_name = 'chafik'
        self.assertEqual(self.obj.first_name, 'sara')
        self.assertEqual(self.obj.last_name, 'chafik')

    def test_str(self):
        """test for __str__ method of BaseModel
        """
        to_str = str(self.obj)
        obj_id = "[{}] ({}) {}".format(
                self.obj.__class__.__name__, self.obj.id, self.obj.__dict__)
        test = obj_id in to_str
        self.assertEqual(True, test)
        test = "updated_at" in to_str
        self.assertEqual(True, test)
        test = "created_at" in to_str
        self.assertEqual(True, test)
        test = "datetime" in to_str
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.obj.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.obj.created_at.isoformat())
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.obj.__class__.__name__)
        self.assertEqual(my_dict['id'], self.obj.id)

    def test_unique_id(self):
        """test for id in BaseModel objects
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(self.obj.id, obj1.id)
        self.assertNotEqual(self.obj.id, obj2.id)

    def test_custom_id(self):
        """Test if BaseModel uses a provided ID correctly
        """
        custom_id = "custom_id"
        obj = BaseModel(id=custom_id)
        self.assertEqual(obj.id, custom_id)

    def test_id_type_string(self):
        """test id in BaseModel is a string
        """
        self.assertEqual(type(self.obj.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        T1 = self.obj.updated_at
        self.obj.save()
        T2 = self.obj.updated_at
        self.assertNotEqual(T1, T2)
        self.assertEqual(type(T1), datetime)
