#!/usr/bin/python3
"""A module who is a base class of descendants classes.
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Define the general attributes and methods of subclasses.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new Object.
            Attributes:
            args (list): inputted arguments as a list.
            kwargs (dict): inputted arguments as a dict.
            id (str) - assign with an uuid when an instance is created.
            created_at (time): datetime - assign with the current datetime when
                an instance is created.
            updated_at (time): datetime - assign with the current datetime when
                n instance is created and it will be updated every time you
                change your object.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def save(self):
        """Update the object.
        Returns:
            none.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """All keys values of the dict.
        Returns:
            Dictionnar containeing all keys and values.
        """
        classDict = dict(self.__dict__)
        classDict['__class__'] = __class__.__name__
        classDict['created_at'] = self.created_at.isoformat()
        classDict['updated_at'] = self.updated_at.isoformat()
        return classDict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
    
    def __str__(self):
        """Return the printable representation of the model.
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
