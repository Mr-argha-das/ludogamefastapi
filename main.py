from fastapi import FastAPI, HTTPException
from mongoengine import connect
from usermodel import UserModel, UserJsonModel, UserloginModel
from userbalance import UserBalance, UserBalanceJsonModel, UserWithdrawalReq
from userwithdrawal import UserWithdrawal
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
async def Sginup(userJson: UserJsonModel):
    user = UserModel(enloginid=userJson.enloginid, upid=userJson.upid)
    user.save()
    data = user.to_json()
    data2 = json.loads(data)
    return {
        "message":"user created success",
        "data":data2,
        "status":True
    }
    
@app.post("/user-login")
async def userLogin(userJson: UserloginModel):
    userdata = UserModel.objects(enloginid=userJson.enLoginid).first()
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
async def addUesrBalance(item: UserBalanceJsonModel):
    addUserBl = UserBalance(user_id=item.user_id, balance=item.balance)
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
        
@app.post("/withdrawal-req")
async def withdrawalreq(item: UserWithdrawalReq):
    usercurrent = UserBalance.objects(user_id=item.userid).first()
    if usercurrent.balance > item.amount:
        userWithdrawal = UserWithdrawal(userid=item.userid, name=item.name, amount=item.amount)
        a = usercurrent.balance - item.amount
        userWithdrawal.save()
        usercurrent.balance = a
        usercurrent.save()
        tojson = usercurrent.to_json()
        fromjson = json.loads(tojson)
        
        return {
            "message":"Your requesit succes ",
            "data": fromjson,
            "status":True
        }
    else:
        return {
            "message":"In your wallet you not have ammount to withdrawal",
            "data": None,
            "status":True
        }
        

@app.get("/all-withdrawal-req-list")
async def withdrawalreqlist():
    userdata = UserWithdrawal.objects.all()
    tojson = userdata.to_json()
    fromjson = json.loads(tojson)
    return {
        "data": fromjson,
        "status":True
    }