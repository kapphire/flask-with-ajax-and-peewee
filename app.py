from flask import Flask, render_template, request, jsonify
from peewee import *
import json
from dbconnection import connection

database = MySQLDatabase('pythonprogramming', host = 'localhost', user = 'root', password = '')

app = Flask(__name__)

class BaseModel(Model):
    class Meta:
        database = database


class Country(BaseModel):
    country_name = CharField(unique=True, max_length=50)

    class Meta:
        order_by = ('country_name',)


class State(BaseModel):
    country = ForeignKeyField(Country, related_name='states')
    state_name = CharField(max_length=50)

    class Meta:
        order_by = ('state_name',)


class City(BaseModel):
    state = ForeignKeyField(State, related_name='cities')
    city_name = CharField(max_length=50)

    class Meta:
        order_by = ('city_name',)


class Content(BaseModel):
	city = ForeignKeyField(City, related_name='contents')
	title = CharField(max_length=255)
	your_name = CharField(max_length=50)
	ad_type = SmallIntegerField()
	payment_type = SmallIntegerField()
	website = TextField()
	price = FloatField()
	currency = SmallIntegerField()
	captcha = TextField()

	class Meta:
		order_by = ('your_name',)


@app.route('/create_database')
def create_tables():
    database.connect()
    database.create_tables([Country, State, City, Content])
    return('Database completed')

@app.route('/')
def upload():
    return render_template('newads.html')


@app.route('/ajaxData/', methods = ['POST'])
def ajaxData():
	adTitle=request.json['adTitle']
	jobTitle=request.json['jobTitle']
	adType=request.json['adType']
	payType=request.json['payType']
	website=request.json['website']
	adPrice=request.json['adPrice']
	currency=request.json['currency']
	country=request.json['country']
	state=request.json['state']
	city=request.json['city']
	adDetail=request.json['adDetail']

	conn = connection()

	with conn.transaction():
		content = Content.create(
			title=adTitle,
			your_name=jobTitle,
			ad_type=adType,
			payment_type=payType,
			website=website,
			price=adPrice,
			currency=currency,
			captcha=adDetail)
		city = City.create(
        	city_name = city)
		state = State.create(
        	state_name = state)
		country = Country.create(
        	country_name = country)

	return jsonify(title = adTitle)


if __name__ == '__main__':
    
    app.debug = True
    app.run()