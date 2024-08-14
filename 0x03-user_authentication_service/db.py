#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


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
        """Add a new user to the database

        Args:
            email (str): The user's email address
            hashed_password (str): The user's hashed password

        Returns:
            User: The newly created User object
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **fillter) -> User:
        '''find user based on filter'''
        filter_fields, filter_values = [], []
        for field, value in filters.items():
            if hasattr(User, field):
                filter_fields.append(getter(User, field))
                filter_values.append(value)
            else:
                raise InvalidRequestError(f"Invalid filter:{field}")
            user = self._session.quary(User).filter(
                tuple_(*filter_fields).in_([tuple(filter_values)])
            ).first()
            if user is None:
                raise NoResultFound("User not found.")
            return user