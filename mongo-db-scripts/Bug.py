from mongoengine import *

class Change(EmbeddedDocument):
    added = StringField()
    field_name = StringField()
    removed = StringField()

class Changes(EmbeddedDocument):
    when = DateTimeField()
    who = StringField()
    changes = DictField()

class Creator(EmbeddedDocument):
    email = StringField()
    id = IntField()
    name = StringField()
    real_name = StringField()
    nick = StringField()

class Bug(Document):
    bug_id = IntField(required = True, unique = True)
    resolution = StringField()
    last_change_time = DateTimeField()
    history = ListField(DictField())
    creator = StringField()
    creator_detail = DictField()
    comments = DictField()
    summary = StringField()