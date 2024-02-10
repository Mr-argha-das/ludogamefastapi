from fastapi import FastAPI, HTTPException
from mongoengine import connect
from usermodel import UserModel
from userbalance import UserBalance
import json

app = FastAPI()

connect('simpleLudo', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/simpleLudo")

@app.get("/user-list")
async def userLsit():
    user = UserModel.objects.all()
    tojson = user.to_json()
    fromjson = json.loads(tojson)
    return fromjson

@app.post("/create-user")
async def Sginup(enloginid: str, upid: str):
    user = UserModel(enloginid=enloginid, upid=upid)
    user.save()
    data = user.to_json()
    data2 = json.loads(data)
    return {
        "message":"user created success",
        "data":data2,
        "status":True
    }
    
@app.post("/user-login")
async def userLogin(enloginid: str):
    userdata = UserModel.objects(enloginid=enloginid).first()
    data = userdata.to_json()
    jsondata = json.loads(data)
    if userdata:
        {
            "message":"User Login success",
            "data":jsondata,
            "status":True,
        }
    return  {
            "message":"User Login faild",
            "data":None,
            "status":False,
        }
        
        
@app.post("/add-user-balance")
async def addUesrBalance(userId: str, balance: float):
    addUserBl = UserBalance(user_id=userId, balance=balance)
    addUserBl.save()
    return {
        "message":"User balance add",
        "status":True
    }
    
@app.get("/user-balance/{userid}")
async def getUserBalance(userid: str):
    balance = UserBalance.objects(user_id=userid).first()
    tojson = balance.to_json()
    fromjson = json.loads(tojson)
    if balance:
        return {
            "message":"Here is your balance",
            "data":fromjson,
            "status": True,
        }
    return {
        "message":"Balance not added yet",
        "data":None,
        "status":False
    }
@app.put("/update-balance/{userid}/{value}")
async def updatebalance(userid: str, value: bool, amount: float):
    balance = UserBalance.objects(user_id=userid).first()
    if value == True:
        currentBalance = balance.balance
        balance.balance = currentBalance+amount
        balance.save()
        tojson = balance.to_json()
        fromjson = json.loads(tojson)
        return {
            "message":"Balance updated",
            "data": fromjson,
            "status": True,
        }
    else:
        currentBalance = balance.balance
        a =  currentBalance-amount
        if a < 0:
            return {
                "message": "You dont have enghop amount to play",
                "data": None,
                "status":False
            }
        balance.balance = a
        balance.save()
        tojson = balance.to_json()
        fromjson = json.loads(tojson)
        return {
            "message":"Balance updated",
            "data": fromjson,
            "status": True,
        }
            