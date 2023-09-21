from __future__ import annotations
from . import db, ma
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_marshmallow import fields


class Movie(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    opinion = db.Column(db.Integer, db.ForeignKey('Opinion._id'))
    description = db.Column(db.String(100), unique=False)

    def __init__(self, title, opinion, description):
        self.name, self.opinion, self.description = title, opinion, description


class Opinion(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), unique=True)

    def __init__(self, content):
        self.content, self.movie_id = content
