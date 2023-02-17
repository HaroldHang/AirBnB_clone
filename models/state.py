#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.city import City
from os import getenv


class State(BaseModel):
    """ State class """
    name = ""
    cities = ""