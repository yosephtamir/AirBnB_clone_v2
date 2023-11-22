#!/usr/bin/python3
"""This is a database engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """Initial point"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """DataBase query"""
        if cls is None:
            inst = self.__session.query(State).all()
            inst.extend(self.__session.query(City).all())
            inst.extend(self.__session.query(User).all())
            inst.extend(self.__session.query(Place).all())
            inst.extend(self.__session.query(Review).all())
            inst.extend(self.__session.query(Amenity).all())
        else:
            inst = self.__session.query(cls)
        return {"{}.{}".format(type(attr).__name__, attr.id):
                attr for attr in inst}

    def new(self, obj):
        """to db"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """used to commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Used to destroy an object from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Used to retrive"""
        Base.metadata.create_all(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """Close the Session
        """
        self.__session.close()
