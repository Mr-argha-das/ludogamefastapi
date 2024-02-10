from mongoengine import Document, StringField, DateTimeField, IntField, BooleanField
from datetime import datetime
class UserWithdrawal(Document):
    userid = StringField(required=True, max_length=200)
    name = StringField(required=True, max_length=200)
    trnx = StringField(required=False, max_length=200)
    amount = IntField(required=True)
    status = BooleanField(default=False)
    created = DateTimeField(default=datetime.today())
    updateat = DateTimeField(default=datetime.today())