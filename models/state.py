#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = ""
    cities = ""