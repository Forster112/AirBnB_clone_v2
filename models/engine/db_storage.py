#!/usr/bin/python3
"""DBStorage Module"""
import os
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User


class DBStorage:
    """Class for DB storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize db storage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER", default=None),
                os.getenv("HBNB_MYSQL_PWD", default=None),
                os.getenv("HBNB_MYSQL_HOST", default=None),
                os.getenv("HBNB_MYSQL_DB", default=None)),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current dataase session"""

        ses_dict = {}

    def new(self, obj):
        """adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session
