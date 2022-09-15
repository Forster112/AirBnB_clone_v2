#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""
        
    @property
    def cities(self):
        """Get cities by state"""
        city_list = []
        cities = models.storage.all(City)
        for city in cities:
            if cities[city].state_id == self.id:
                city_list.append(cities[city])
        return city_list
