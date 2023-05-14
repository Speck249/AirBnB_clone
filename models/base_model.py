#!/usr/bin/python3
"""Module creates class BaseModel."""
import uuid
import models
from datetime import datetime

class BaseModel():
    """Empty class created."""

    def __init__(self, *args, **kwargs):
        """Method initializes attributes.

        Args:
            args: non-keyworded argument list.
            kwargs: keyworded argument list
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs != {} and kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, \
                            tformat)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Method prints string representation."""

        return ("[{}] ({}) {}".
                format(self.__class__.__name__,
                       self.id, self.__dict__))

    def save(self):
        """Method updates attribute updated_at."""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Method returns dictionary representation."""

        dict_rep = {}

        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()

        return dict_rep
