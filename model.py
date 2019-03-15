""" In this module all the models necessary for the creation of tables 
	in database are defined."""


# All the SQL commands are written using peewee
# Therefore importing the peewee package 
from peewee import *

# Creating a database called easy_pay
db = SqliteDatabase('easy_pay.db')


''' This  customer model is used to create the rows of the table consisting 
	of the following customer details:
		* first name
		* last name
		* email id
		* phone number
		* user name 
		*password
'''
class Customer(Model):
	first_name = TextField()
	last_name = TextField()
	email_id = TextField()
	phone_number = TextField()
	user_name = TextField(unique = True)
	password = TextField()

	class Meta:
		database = db 

''' The Card_details model is used to create rows of the table consisting of the 
	following card_details:
		* card holder name
		* card number
		* card expiry month
		* card expiry year
		* card cvv
	Note: Customer is a foreign key field that relates the customer table with 
		  card details 
'''
class Card_details(Model):
	customer = ForeignKeyField(Customer, default = True)
	card_holder_name = TextField()
	card_number = TextField(unique = True)
	expiry_month = TextField()
	expiry_year = TextField()
	cvv = TextField()

	class Meta:
		database = db

# To connect to the database easy_pay.db 
db.connect()

# This command creates the tables for models defined above
db.create_tables([Customer,Card_details])