from mongoengine import Document, StringField, DateTimeField, BooleanField

class UserModel(Document):
    enloginid = StringField(required=True, max_length=200)
    upid = StringField(required=False, max_length=200)
    status = BooleanField(default=True)
    