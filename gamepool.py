from mongoengine import Document, StringField, FloatField

class GamePool(Document):
    investment = FloatField(required=True, max_length=200)
    persion1 = FloatField(required=True, max_lenght=200)
    persion2 =  FloatField(required=True, max_lenght=200)
    persion3 = FloatField(required=True, max_lenght=200)
    persion4 = FloatField(required=True, max_lenght=200)
    totalamount = FloatField(required=True, max_lenght=200)
    ourincome = FloatField(required=True, max_length=200)