#!/usr/bin/python3
"""Unit test for Place"""

import unittest
import models
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test for Place class"""

    def test_docstring(self):
        """This is a test to check if functions,
        classes and modules all have docstring"""
        message = "Docstring is not present in function"
        self.assertIsNotNone(models.place.__doc__, message)
        message = "Docstring is not present in class"
        self.assertIsNotNone(Place.__doc__, message)

    def test_exec_file(self):
        """check if all files are executable"""

        read_true = os.access("models/place.py", os.R_OK)
        self.assertTrue(read_true)

        write_true = os.access("models/place.py", os.W_OK)
        self.assertTrue(write_true)

        exec_true = os.access("models/place.py", os.X_OK)
        self.assertTrue(exec_true)

    def test_init_Place(self):
        """check if object is Place"""
        check_Place = Place()
        self.assertIsInstance(check_Place, Place)

    def test_id(self):
        """Check if the ids are unique"""
        first_id = Place()
        second_id = Place()
        self.assertNotEqual(first_id, second_id)

    def test_str(self):
        """Check if the output is a string"""
        str_obj = Place()
        dictionary = str_obj.__dict__
        first_str = "[Place] ({}) {}".format(str_obj.id, dictionary)
        second_str = str(str_obj)
        self.assertEqual(first_str, second_str)

    def test_save(self):
        """Check if date update is save"""
        updated = Place()
        first_update = updated.updated_at
        updated.save()
        second_update = updated.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        """Check if to_dict added a dictionary"""
        original_model = Place()
        dict_model = original_model.to_dict()
        self.assertIsInstance(dict_model, dict)
        for key, value in dict_model.items():
            check = 0
            if dict_model['__class__'] == 'Place':
                check += 1
            self.assertTrue(check == 1)
        for key, value in dict_model.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
