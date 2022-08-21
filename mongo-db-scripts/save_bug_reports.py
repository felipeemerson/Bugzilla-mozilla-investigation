from mongoengine import *
from Bug import Bug
import json

connect('bug_reports_db', host='127.0.0.1', port=27017)

with open('base\\bugs_base_final.json') as input:
  bugs = json.load(input)

for bug in bugs:
  bug = Bug(**bug)
  bug.save()