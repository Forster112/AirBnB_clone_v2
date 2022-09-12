#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    name = ""

    @getter
    def cities():
        city_list = []
        for city in models.storage.all(City):
            print(city)
            if city.state_id == State.id:
                city_list.append(city)
        return city_list
