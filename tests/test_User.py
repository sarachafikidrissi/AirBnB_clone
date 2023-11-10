import unittest
from models.user import User
from models.base_model import Base_model

class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """
    def test_user_creation_default_values(self):
        """
        Test User creation with default values.
        """
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_user_creation_with_values(self):
        """
        Test User creation with provided values.
        """
        user = User(email='john@example.com', password='password123', first_name='John', last_name='Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_str_method(self):
        """
        Test the __str__ method.
        """
        user = User(email='john@example.com', password='password123', first_name='John', last_name='Doe')
        expected_str = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method.
        """
        user = User(email='john@example.com', password='password123', first_name='John', last_name='Doe')
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'john@example.com')
        self.assertEqual(user_dict['password'], 'password123')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

    def test_user_creation_with_invalid_values(self):
        """
        Test User creation with invalid values.
        """
        with self.assertRaises(ValueError):
            user = User(email=123, password=456, first_name=True, last_name=None)

if __name__ == '__main__':
    unittest.main()

