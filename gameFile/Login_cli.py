import inquirer
from game import *
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship, backref, declarative_base

Base = declarative_base()

class User(Base):
    pass

class Score(Base):
    pass


