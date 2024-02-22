from datetime import datetime

from peewee import SqliteDatabase, Model, DateField, TextField

db = SqliteDatabase('lecture.db')
class ModelBase(Model):
    created_at = DateField(default=datetime.now())

    class Meta():
        database = db

class History(ModelBase):
    number = TextField()
    message = TextField()
