from application import db

class Counter(db.Document):
    count = db.IntField(db_field="c")
    two =db.IntField(db_field="t")