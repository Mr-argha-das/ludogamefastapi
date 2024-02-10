from mongoengine import Document, StringField, DateTimeField, FloatField, BooleanField

class UserBalance(Document):
    user_id = StringField(required=True, max_length=200)
    balance = FloatField(required=True, max_length=200)
    status = BooleanField(required=True, default=True)