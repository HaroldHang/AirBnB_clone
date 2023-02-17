#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from os import getenv
import models

class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    
    
    @property
    def reviews(self):
        """ Returns list of reviews.id """
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            review = key.replace('.', ' ')
            review = shlex.split(review)
            if (review[0] == 'Review'):
                lista.append(var[key])
        for elem in lista:
            if (elem.place_id == self.id):
                result.append(elem)
        return (result)
    @property
    def amenities(self):
        """ Returns list of amenity ids """
        return self.amenity_ids
    @amenities.setter
    def amenities(self, obj=None):
        """ Appends amenity ids to the attribute """
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)