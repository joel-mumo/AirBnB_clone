#!/usr/bin/python3
"""Unit test for Amenity"""

import unittest
import models
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test for Amenity class"""

    def test_docstring(self):
        """This is a test to check if functions,
        classes and modules all have docstring"""
        message = "Docstring is not present in function"
        self.assertIsNotNone(models.amenity.__doc__, message)
        message = "Docstring is not present in class"
        self.assertIsNotNone(Amenity.__doc__, message)

    def test_exec_file(self):
        """check if all files are executable"""
        read_true = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(read_true)

        write_true = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(write_true)

        exec_true = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(exec_true)

    def test_init_Amenity(self):
        """check if object is Amenity"""
        check_Amenity = Amenity()
        self.assertIsInstance(check_Amenity, Amenity)

    def test_id(self):
        """Check if IDs are unique"""
        first_id = Amenity()
        second_id = Amenity()
        self.assertNotEqual(first_id, second_id)

    def test_str(self):
        """Check if the output is a string"""
        str_obj = Amenity()
        dictionary = str_obj.__dict__
        first_str = "[Amenity] ({}) {}".format(str_obj.id, dictionary)
        second_str = str(str_obj)
        self.assertEqual(first_str, second_str)

    def test_save(self):
        """Check if date update is saved"""
        updated = Amenity()
        first_update = updated.updated_at
        updated.save()
        second_update = updated.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        """Check if to_dict added a dictionary"""
        original_model = Amenity()
        dict_model = original_model.to_dict()
        self.assertIsInstance(dict_model, dict)
        for key, value in dict_model.items():
            check = 0
            if dict_model['__class__'] == 'Amenity':
                check += 1
            self.assertTrue(check == 1)
        for key, value in dict_model.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
