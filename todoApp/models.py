import os
import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('postgres_secret')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class TodoModel(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = db.Column(db.String())
    name = db.Column(db.String())
    complete = db.Column(db.Boolean)

    def __init__(self, content, name, complete):
        self.content = content
        self.name = name
        self.complete = complete

    def __repr__(self):
        return f"Task id {self.id}"
