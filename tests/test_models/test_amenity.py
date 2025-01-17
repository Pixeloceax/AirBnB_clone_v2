#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(type(new.name), str)
