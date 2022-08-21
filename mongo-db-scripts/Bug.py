from mongoengine import *

class Bug(Document):
    bug_id = IntField(required = True, unique = True)
    resolution = StringField()
    last_change_time = DateTimeField()
    history = ListField(DictField())
    creator = StringField()
    creator_detail = DictField()
    comments = DictField()
    summary = StringField()