'''This program consists of the following functions:
		* add the customer entries -->signup
		* login by the customer
		* add the card details 
		* retriving the card details from the database basedon phone number'''

# Importing the models customer and card_details from the model.py module
from model import *

# This function 
def signup(f_firstname, f_lastname, f_email_id ,f_phone_no ,f_username ,f_password):
	firstname = f_firstname
	lastname = f_lastname
	email_id = f_email_id
	phone_no = f_phone_no
	username = f_username
	password = f_password

	print("Created New Sign Up")
	try:
		print("creating")
		Customer.create(first_name = firstname, last_name = lastname, email_id = email_id ,phone_number = phone_no, user_name = username, password = password)
	except:
		print("updating")
		Customer.update(first_name = firstname, last_name = lastname, email_id = email_id ,phone_number = phone_no, user_name = username, password = password)
	print("updated to db")



def login(f_username, f_password):

	username = f_username
	password = f_password

	print(username)
	print(password)

	try:
		query1 = Customer.select().where(Customer.user_name == username)

		if ((password == query1[0].password) and (query1[0].user_name == username)):
			print("loged In")
			# return True
		else:
			print("Invalid username or password")
			#return False

	except:
		print("user does not exist")
		# return False

	

def card(f_card_holder,f_card_no,f_exp_month,f_exp_year,f_cvv):

	card_holder_name1 = f_card_holder
	card_number1 = f_card_no
	expiry_month1 = f_exp_month
	expiry_year1 = f_exp_year
	cvv1 = f_cvv
	print(card_number1)

	print("card details ")
	
	c = Card_details.create(card_holder_name = card_holder_name1, card_number = card_number1, expiry_month = expiry_month1 ,expiry_year = expiry_year1 , cvv = cvv1)
	print("working")

	# except:
	# 	Card_details.update(card_holder_name = card_holder_name1, card_number = card_number1, expiry_month = expiry_month1 ,expiry_date = expiry_date1 ,cvv = cvv1)
	# 	Card_details.save()
	# 	print("card details added to db")



def select_card_holder(phone_no):


	user = Customer.get(Customer.phone_number == phone_no)
#	print(type(user))
	user_card_details = Card_details.select().where(Card_details.customer == 1)
	print(user_card_details[0].card_holder_name)
	print(user_card_details[0].card_number)
	print(user_card_details[0].expiry_month)
	print(user_card_details[0].expiry_year)
	print(user_card_details[0].cvv)
	# print(len(user_card_details))
	# user_card_details = Card_details.select().join(Customer).where(Customer.phone_number == phone_no)

	# user = Customer.select().where(Customer.phone_number == phone_no)
	# print(user)
	# user_card_details = Card_details.select().where(Card_details.customer == user)
	# print(len(user_card_details))


	# print(user_card_details.card_holder_name)
	# print(user)
	# user_card_details = Card_details.select().join(Customer).where(Customer.phone_number == phone_no)
	# for detail in user_card_details:
	# 	print(detail)
	# 	print(detail.card_number, detail.card_holder_name, detail.expiry_month, detail.expiry_year,detail.cvv)
	# 	return(detail.card_holder_name,detail.card_number,detail.expiry_month, detail.expiry_year,detail.cvv)



# signup("rakesh","r","rakeshr2552@gmail.com","900873470","r125","2552")
# signup("vin","r","vin2552@gmail.com","9008873471","r135","r552")
# signup("prajwal","s","prajwalvrvmp@gmail.com","7019740371","prajju","PJ")

# login("r15","2552")
#login("r135","r552")
#login("prajju","PJ")


#user = Customer.get(Customer.id == 2)


# card("rak","5254561445",12,20,511)
# card("vin","521",1,2,602)
# card("praj","5254561",1,10,516)


#print(Card_details.customer.phone_number)

select_card_holder("9008873471")
