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
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """Get cities by state"""
            city_list = []
            for city in list(models.storage.all(City).items()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
