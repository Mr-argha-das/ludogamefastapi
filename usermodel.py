from mongoengine import Document, StringField, DateTimeField, BooleanField
from pydantic import BaseModel

class UserModel(Document):
    enloginid = StringField(required=True, max_length=200)
    upid = StringField(required=False, max_length=200)
    status = BooleanField(default=True)


class UserJsonModel(BaseModel):
    enloginid: str
    upid: str



class UserloginModel(BaseModel):
    enloginid: str