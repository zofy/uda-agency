import contextlib
import enum
import os
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.exc import SQLAlchemyError

DATE_FORMAT = "%Y-%m-%d"
db = SQLAlchemy()


class GenderType(enum.Enum):
    MALE = 1
    FEMALE = 2


@contextlib.contextmanager
def db_rollback():
    try:
        yield
    except SQLAlchemyError:
        db.session.rollback()
        raise


class DBOperationsMixin:
    def insert(self):
        with db_rollback():
            db.session.add(self)
            db.session.commit()

    def update(self):
        with db_rollback():
            db.session.commit()

    def update_by_mapping(self, mapping):
        for k, v in mapping.items():
            if k not in self.__dict__:
                raise ValueError(f"Invalid mapping for {self.__class__}")
            setattr(self, k, v)
        self.update()

    def delete(self):
        with db_rollback():
            db.session.delete(self)
            db.session.commit()


class Movie(db.Model, DBOperationsMixin):
    __tablename__ = "movies"
    id = Column(Integer(), primary_key=True)
    title = Column(String(150), nullable=False, unique=True)
    release_date = Column(DateTime(), nullable=False)

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": datetime.strftime(self.release_date, DATE_FORMAT),
        }


class Actor(db.Model, DBOperationsMixin):
    __tablename__ = "actors"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    age = Column(Integer(), nullable=False)
    gender = Column("gender", Enum(GenderType), nullable=False)

    def format(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "gender": self.gender.name,
        }
