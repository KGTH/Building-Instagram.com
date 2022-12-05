import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True )
    name = Column(String(80), nullable=False)
    last_name= Column(String(80), nullable=False)
    telephone= Column(Integer)
    email= Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)



class Image_post(Base):
    __tablename__ = 'image_post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))
    title= Column(String(250))
    url= Column(String(250), nullable=False)
    comment= Column(String(250))
   

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))
    id_post=Column(Integer, ForeignKey('image_post.id'))
    text=Column(String(250))

class likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_image = Column(Integer, ForeignKey('image_post.id'))
    likes= Column(String(250))
    unlikes= Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
