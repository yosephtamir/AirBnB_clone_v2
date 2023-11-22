#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    @property
    def cities(self):
        if getenv("HBNB_TYPE_STORAGE") != "db":
            """This is used to return associated cities with current state"""
            files = list(models.storage.all(City).values())
            sameList = []
            for attr in files:
                if attr.state_id == self.id:
                    sameList.append(attr)
            return attr
