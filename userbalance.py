from mongoengine import Document, StringField, DateTimeField, FloatField, BooleanField
from pydantic import BaseModel
class UserBalance(Document):
    user_id = StringField(required=True, max_length=200)
    balance = FloatField(required=True, max_length=200)
    status = BooleanField(required=True, default=True)


class UserBalanceJsonModel(BaseModel):
    user_id:str
    balance: str

class UserWithdrawalReq(BaseModel):
    userid: str
    name: str
    amount: float