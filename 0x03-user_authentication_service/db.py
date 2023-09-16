#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError, IntegrityError

from user import Base
from user import User
import uuid

def generate_session_id():
    """function for generating the unique id"""
    return str(uuid.uuid4())


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Fundtion that adds a new user to the database
        """
        session_id = generate_session_id()
        new_user = User(email=email, hashed_password=hashed_password, session_id=session_id)
        self._session.add(new_user)
        try:
            self._session.commit()
        except IntegrityError:
            #self._session.rallback()
            raise Exception("user alreay exists")
        return new_user

    def find_user_by(self, **kwargs):
        """Funtion for finding a user"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("Not Found")
            return user
        except InvalidRequestError as e:
            raise e

    def update_user(self, user_id, **kwargs):
        """Updates user details using the privided user_id
        """
        try:
            user = self._session.query(User).filter_by(id=user_id).one()
            for key, value in kwargs.items():
                setattr(user, key, value)
                return user
        except NoResultFound:
            raise NoResultFound("No user found with the user_id")
        except InvalidRequestError as e:
            raise e
