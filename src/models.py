import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class UserFollowers(Base):
    __tablename__ = "user_followers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    total_likes = Column(Integer, nullable=False)
    total_comments = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class PostLikes(Base):
    __tablename__ = "post_likes"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class PostComments(Base):
    __tablename__ = "post_comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String, nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class UserFeeds(Base):
    __tablename__ = "user_feeds"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
