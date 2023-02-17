#!/usr/bin/python3
""" """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
from uuid import UUID
import json
import os

import unittest

class TestBaseModel(unittest.TestCase):
    def test_id(self):
        baseModel1 = BaseModel()
        baseModel2 = BaseModel()
        self.assertTrue(baseModel1.id != baseModel2.id)
    """
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    """
    def test_recreate(self):
        baseModel1 = BaseModel()
        baseModel2 = BaseModel(**(baseModel1.to_dict()))
        self.assertTrue(baseModel1.id != baseModel2.id)
if __name__ == '__main__':
    unittest.main()