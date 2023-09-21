from __future__ import annotations
from . import db, ma
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_marshmallow import fields


class Movie(db.Model):
    __tablename__ = 'movie'
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(100), unique=False)
    opinions = db.relationship('Opinion', backref='opinions', lazy=True)

    def __init__(self, title, description):
        self.title, self.description = title, description


class Opinion(db.Model):
    __tablename__ = 'opinion'
    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), unique=True)
    movie = db.Column(db.Integer, db.ForeignKey('movie._id'))

    def __init__(self, content, movie_id):
        self.content, self.movie = content, movie_id
