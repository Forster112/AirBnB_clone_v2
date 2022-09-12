#!/usr/bin/python3
"""DBStorage Module"""
import os
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from models.base_model import Base


class DBStorage:
    """Class for DB storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize db storage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"\
                                      .format(os.getenv("HBNB_MYSQL_USER", default=None),
                                              os.getenv("HBNB_MYSQL_PWD", default=None),
                                              os.getenv("HBNB_MYSQL_HOST", default=None),
                                              os.getenv("HBNB_MYSQL_DB", default=None)),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        session = Session()
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
