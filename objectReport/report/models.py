from mongoengine import Document, fields

class Report(Document):
    pid = fields.StringField(required=True)
    classId = fields.StringField(required=True)
    classObject = fields.DictField(required=True)
