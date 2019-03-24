from peewee import *
from os import environ

host = environ.get("SERVER")

db = MySQLDatabase(
    host=host, port=3303, passwd="shellshell", user="shell", database="shell"
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Purchase(BaseModel): 
    date = DateTimeField() 
    price = FloatField() 
    qtd = IntegerField() 
    station = CharField()
    product = CharField()
    
    class Meta: 
        table_name = "purchases"

class LastProduct(BaseModel):
    name = CharField()

    class Meta:
        table_name = "last_product"