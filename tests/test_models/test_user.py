#!/usr/bin/python3
"""Unit test for User"""

import unittest
import models
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test for User class"""

    def test_docstring(self):
        """This is a test to check if functions,
        classes and modules all have docstring"""
        message = "Docstring is not present in function"
        self.assertIsNotNone(models.user.__doc__, message)
        message = "Docstring is not present in class"
        self.assertIsNotNone(User.__doc__, message)

    def test_exec_file(self):
        """check if all files are executable"""

        read_true = os.access("models/user.py", os.R_OK)
        self.assertTrue(read_true)

        write_true = os.access("models/user.py", os.W_OK)
        self.assertTrue(write_true)

        exec_true = os.access("models/user.py", os.X_OK)
        self.assertTrue(exec_true)

    def test_init_User(self):
        """check if object is User"""
        check_User = User()
        self.assertIsInstance(check_User, User)

    def test_id(self):
        """Check if the ids are unique"""
        first_id = User()
        second_id = User()
        self.assertNotEqual(first_id, second_id)

    def test_str(self):
        """Check if the output is a string"""
        str_obj = User()
        dictionary = str_obj.__dict__
        first_str = "[User] ({}) {}".format(str_obj.id, dictionary)
        second_str = str(str_obj)
        self.assertEqual(first_str, second_str)

    def test_save(self):
        """Check if date update is saved"""
        updated = User()
        first_update = updated.updated_at
        updated.save()
        second_update = updated.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        """Check if to_dict added a dictionary"""
        original_model = User()
        dict_model = original_model.to_dict()
        self.assertIsInstance(dict_model, dict)
        for key, value in dict_model.items():
            check = 0
            if dict_model['__class__'] == 'User':
                check += 1
            self.assertTrue(check == 1)
        for key, value in dict_model.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
