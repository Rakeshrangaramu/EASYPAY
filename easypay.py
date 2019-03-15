"""Import the required modules and files for the program.
Tkinter is used as a frontend module.
Pyautogui is used for automation functions.
PeeWee and model are used for using database"""
import tkinter as tk
import tkinter.messagebox
import os
from tkinter import *
from peewee import *
# Importing the models customer and card_details from the model.py module
from model import *

class EasyPayApp(tk.Tk):
	"""The class is instantiated. This creates a toplevel 
	widget of Tk which usually is the main window of an application which is developed to automate the recursive things."""

	def __init__(self):
		
		#Initializing the object for window.
		tk.Tk.__init__(self)
		
		#Title of the window.
		self.title("EASYPAY")
		
		#Shape of the window.
		self.geometry("1366x768+10+10")

		#Creating canvas for the window.
		self.C = tk.Canvas(self, bg="blue")
		self.filename = PhotoImage(file = "bg.gif")
		self.background_label = Label(self, image=self.filename)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.C.pack()

		#Initializing required components like buttons,labels and entry boxes.
		self.photo = PhotoImage(file="speckbit.gif")
		self.speckbit = tk.Label(self, image=self.photo,anchor=CENTER)
		self.speckbit.pack()
		self.speckbit.place(x=30,y=80)
		
		#Create an entry box and label it to get the username of the user.
		self.entry1=tk.Entry(self,width=30)
		self.entry1.pack()
		self.entry1.place(x=600,y=300)

		self.usern=tk.Label(self,text="Username:",anchor=CENTER,font="sansserif 10")
		self.usern.pack()
		self.usern.place(x=523,y=297)

		#Create an entry box and label it to get the password of the user.
		self.entry2=tk.Entry(self,width=30,show="*")
		self.entry2.pack()
		self.entry2.place(x=600,y=340)

		self.passw=tk.Label(self,text="Password:",anchor=CENTER,font="sansserif 10")
		self.passw.pack()
		self.passw.place(x=523,y=338)

		#Create a submit button which when clicked operates the function given in command.
		self.submit=tk.Button(self,text="SUBMIT",cursor="hand1",activebackground="blue",font="times 10",anchor=CENTER,width=10,command=self.on_submit)
		self.submit.pack()
		self.submit.place(x=590,y=380)

		#Create a cancel button which when clicked closes the window.
		self.cancel=tk.Button(self,text="CANCEL",cursor="hand1",anchor=CENTER,font="times 10",activebackground="blue",width=10)
		self.cancel.pack()
		self.cancel.place(x=688,y=380)

		#Create a label for new user and a button which when clicked takes the user to signup page.
		self.newuser=tk.Label(self,text="New user?",anchor=CENTER,font="sansserif 10")
		self.newuser.pack()
		self.newuser.place(x=620,y=425)

		self.register=tk.Button(self,text="Sign Up",cursor="hand1",fg="blue",activebackground="blue",bd=0,anchor=CENTER,font="sansserif 10",command=self.on_signup)
		self.register.pack()
		self.register.place(x=685,y=423)

		#Create an about button which when clicked takes user to a page which shows about the application.
		self.about=tk.Button(self,text="About EASYPAY",cursor="hand1",fg="red",bd=0,anchor=CENTER,activebackground="blue",font="sansserif 12",command=self.aboutus)
		self.about.pack()
		self.about.place(x=1200,y=80)
		
	def on_signup(self):
		"""This function describes the components required for the new window which appears after signup button is clicked.
		 The title and geometry of the window is described.A canvas is created which is used to pack and place all other 
		 components of the window.

		 A background image is set using PhotoImage attribute.

		 Additional images to decorate the window are also added using PhotoImage widget 
		 """
		
		#Creating new window
		self.new=tk.Toplevel()

		#Shape of the window.
		self.new.geometry("1366x768")

		#Title of the window.
		self.new.title("SIGN UP")

		#Creating canvas for the window.
		self.D = tk.Canvas(self.new, bg="blue")
		self.bgpic=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.new, image=self.bgpic)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.D.pack()

		#Creating a label for signup picture.
		self.photo1 = PhotoImage(file="signup.gif")
		self.l=tk.Label(self.new,image=self.photo1,anchor=CENTER)
		self.l.pack()
		self.l.place(x=560,y=40)

		#Creating a label for user picture.
		self.photo2 = PhotoImage(file="user.gif")
		self.b1=tk.Label(self.new,image=self.photo2,anchor=NW,bd=0)
		self.b1.pack()
		self.b1.place(x=125,y=125)

		#Creating a label for email picture.
		self.photo3 = PhotoImage(file="email.gif")
		self.b2=tk.Label(self.new,image=self.photo3,anchor=NW,bd=0)
		self.b2.pack()
		self.b2.place(x=160,y=400)

		#Creating a label for password picture.
		self.photo4= PhotoImage(file="password.gif")
		self.b3=tk.Label(self.new,image=self.photo4,anchor=NW,bd=0)
		self.b3.pack()
		self.b3.place(x=950,y=400)

		#Creating a label for phone picture.
		self.photo5 = PhotoImage(file="phone.gif")
		self.b4=tk.Label(self.new,image=self.photo5,anchor=NW,bd=0)
		self.b4.pack()
		self.b4.place(x=900,y=150)

		#Create a label and entry box to get the first name of the user.
		self.l1=tk.Label(self.new,text="First Name:",anchor=CENTER,font="times 14")
		self.l1.pack()
		self.l1.place(x=485,y=176)

		self.e1=tk.Entry(self.new,width=35)
		self.e1.pack()
		self.e1.place(x=645,y=180)

		#Create a label and entry box to get the last name of the user.
		self.l2=tk.Label(self.new,text="Last Name:",anchor=CENTER,font="times 14")
		self.l2.pack()
		self.l2.place(x=485,y=216)

		self.e2=tk.Entry(self.new,width=35)
		self.e2.pack()
		self.e2.place(x=645,y=220)

		#Create a label and entry box to get the email id of the user.
		self.l3=tk.Label(self.new,text="Email Id:",anchor=CENTER,font="times 14")
		self.l3.pack()
		self.l3.place(x=485,y=256)

		self.e3=tk.Entry(self.new,width=35)
		self.e3.pack()
		self.e3.place(x=645,y=260)

		#Create a label and entry box to get the phone no. of the user.
		self.l4=tk.Label(self.new,text="Phone No.:",anchor=CENTER,font="times 14")
		self.l4.pack()
		self.l4.place(x=485,y=296)

		self.e4=tk.Entry(self.new,width=35)
		self.e4.pack()
		self.e4.place(x=645,y=300)

		#Create a label and entry box to get the username of the user.
		self.l5=tk.Label(self.new,text="Username:",anchor=CENTER,font="times 14")
		self.l5.pack()
		self.l5.place(x=485,y=336)

		self.e5=tk.Entry(self.new,width=35)
		self.e5.pack()
		self.e5.place(x=645,y=340)

		#Create a label and entry box to get the password of the user.
		self.l6=tk.Label(self.new,text="Password:",anchor=CENTER,font="times 14")
		self.l6.pack()
		self.l6.place(x=485,y=376)

		self.e6=tk.Entry(self.new,width=35,show="*")
		self.e6.pack()
		self.e6.place(x=645,y=380)

		#Create a label and entry box to get the confirm password of the user.
		self.l7=tk.Label(self.new,text="Confirm Password:",anchor=CENTER,font="times 14")
		self.l7.pack()
		self.l7.place(x=485,y=416)

		self.e7=tk.Entry(self.new,width=35,show="*")
		self.e7.pack()
		self.e7.place(x=645,y=420)

		#Create a submit button which when clicked operates the function given in command.
		self.submit1=tk.Button(self.new,text="SUBMIT",anchor=CENTER,font="times 10",cursor="hand1",width=10,command=self.execu)
		self.submit1.pack()
		self.submit1.place(x=560,y=480)

		#Create a cancel button which when clicked operates the function given in command.		
		self.cancel1=tk.Button(self.new,text="CANCEL",anchor=CENTER,font="times 10",cursor="hand1",width=10,command=self.new.destroy)
		self.cancel1.pack()
		self.cancel1.place(x=750,y=480)

		#This function runs the loop till the user manually closes it.
		mainloop()

	def execu(self):
		"""This function is executed when the submit button on the signup page is pressed.
		This function gets all the details entered in the entry boxes created in the signup page and passes all the details to a
		funtion which adds all those details to the database.
		Also the signup page is destroyed and it takes user back to main home page.
		A message box is poped-up which gives a valid message to user."""

		#The data entered in entry boxes is collected using get funtion and stored in respective variables.
		self.firstname=self.e1.get()            
		self.lastname=self.e2.get()              
		self.email_id=self.e3.get()               
		self.phone_no=self.e4.get()
		self.username=self.e5.get()
		self.password=self.e6.get()
		self.confirmpassinp=self.e7.get()

		#The data in the variables is passed to the function which updates the details in database.
		self.signup(self.firstname,self.lastname,self.email_id,self.phone_no,self.username,self.password)

		#This function destroys the signup page and takes the user to home page.
		self.new.destroy()

		#This function pops up a message box saying 'Signup successful'
		tkinter.messagebox.showinfo("Signup Successful","Please login again with your username and password")

	def on_submit(self):
		"""This function is executed when the submit button is pressed in the home page.
		This function first gets the details in the entryboxes and stores them in variables. 
		those variables are passes to a funtion which verifies whether the user credentials are correct or not.
		If the credential are correct then the user is taken to next options page if not a popup is given with valid message."""

		#The details in the username and password entry boxes are stored in respective variables.
		self.usernameinp = self.entry1.get() 
		self.userpassword=self.entry2.get()

		#The variables are passed to function which verifies credentials whose return value is stored in a variable.
		self.check=self.login(self.usernameinp,self.userpassword)

		#If the return value of variable is true then options page is displayed if not popup message is displayed saying 'Signin unsuccessful'.
		if self.check==True:
			self.option_call()
		else:
			tkinter.messagebox.showinfo("Signin Unsuccessful","Please login again with your valid username and password")

	def option_call(self):
		"""This function is executed when the signin is successful.
		It creates a new window which shows the options for the user.
		Add new card is used to add new card of the user, Mobile recharge is used to proceed to mobile recharge and d2h recharge
		is used to proceed to d2h recharge."""

		#Creating new window
		self.options=tk.Toplevel()

		#Shape of the window.
		self.options.geometry("1366x680")

		#Title of the window.
		self.options.title("OPTIONS")

		#Creating canvas for the window.
		self.E= tk.Canvas(self.options, bg="blue")
		self.bgpic1=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.options, image=self.bgpic1)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.E.pack()

		#Create a button for mobile recharge with a picture on it which operates mobile recharge function when clicked on it.
		self.photo6 = PhotoImage(file="mobile.gif")
		self.mobile=tk.Button(self.options,image=self.photo6,anchor=CENTER,height=220,width=220,bg="light blue",command=self.mobile_recharge)
		self.mobile.pack()
		self.mobile.place(x=175,y=200)

		#Create a button for d2h recharge with a picture on it which operates d2h recharge function when clicked on it.
		self.photo7 = PhotoImage(file="d2h.gif")
		self.d2h=tk.Button(self.options,image=self.photo7,anchor=CENTER,height=220,width=220,bg="light blue",command=self.dth_recharge)
		self.d2h.pack()
		self.d2h.place(x=575,y=200)

		#Create a button for add card function with a picture on it which operates add card function when clicked on it.
		self.photo8 = PhotoImage(file="addcard.gif")
		self.add_card=tk.Button(self.options,image=self.photo8,anchor=CENTER,height=220,width=220,padx=20,bg="light blue",command=self.addcard)
		self.add_card.pack()
		self.add_card.place(x=975,y=200)

		mainloop()

	def addcard(self):
		"""This function is executed when add card button is pressed in options page.
		This function is used to get card details of the user like card holder name, card number, expiry month, expiry year and cvv"""

		#Creating new window
		self.add=tk.Toplevel()

		#Shape of the window.
		self.add.geometry("470x300")

		#Title of the window.
		self.add.title("ADD CARD")

		#Creating canvas for the window.
		self.F= tk.Canvas(self.add, bg="blue")
		self.bgpic=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.add, image=self.bgpic)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.F.pack()

		#Creating a label for card details.
		self.details=tk.Label(self.add,text="CARD DETAILS",anchor=CENTER,font="times 18")
		self.details.pack()
		self.details.place(x=150,y=20)

		#Create a label and entry box to get the name of the card holder.
		self.name=tk.Label(self.add,text="NAME OF CARD HOLDER:",anchor=CENTER,font="times 12")
		self.name.pack()
		self.name.place(x=30,y=70)
		self.e8=tk.Entry(self.add,width=30)
		self.e8.pack()
		self.e8.place(x=230,y=72)

		#Create a label and entry box to get the card number.
		self.number=tk.Label(self.add,text="CARD NUMBER:",anchor=CENTER,font="times 12")
		self.number.pack()
		self.number.place(x=30,y=100)
		self.e9=tk.Entry(self.add,width=16)
		self.e9.pack()
		self.e9.place(x=230,y=102)

		#Create a label and entry box to get the expiry month of the card.
		self.expmonth=tk.Label(self.add,text="EXPIRY MONTH:",anchor=CENTER,font="times 12")
		self.expmonth.pack()
		self.expmonth.place(x=30,y=130)
		self.e10=tk.Entry(self.add,width=2)
		self.e10.pack()
		self.e10.place(x=230,y=132)

		#Create a label and entry box to get the expiry year of the card.
		self.expyear=tk.Label(self.add,text="EXPIRY YEAR:",anchor=CENTER,font="times 12")
		self.expyear.pack()
		self.expyear.place(x=30,y=160)
		self.e11=tk.Entry(self.add,width=2)
		self.e11.pack()
		self.e11.place(x=230,y=162)

		#Create a label and entry box to get the CVV of the card.
		self.cvv=tk.Label(self.add,text="CVV:",anchor=CENTER,font="times 12")
		self.cvv.pack()
		self.cvv.place(x=30,y=190)
		self.e12=tk.Entry(self.add,width=3)
		self.e12.pack()
		self.e12.place(x=230,y=192)

		#Create a submit button which when clicked operates the function given in command.
		self.submit2=tk.Button(self.add,text="SUBMIT",anchor=CENTER,font="times 12",cursor="hand1",width=10,command=self.on_submit_carddetails)
		self.submit2.pack()
		self.submit2.place(x=190,y=230)

		mainloop()

	def aboutus(self):
		"""This function is executed when about us button is pressed on the home page.
		Some information about the application is displayed when executed."""

		#Creating new window
		self.about_us=tk.Toplevel()

		#Shape of the window
		self.about_us.geometry("860x525")

		#Title of the window.
		self.about_us.title("ABOUT US")

		#Creating canvas for the window.
		self.G= tk.Canvas(self.about_us, bg="blue")
		self.bgpicabt=PhotoImage(file="aboutus.gif")
		self.background_label = tk.Label(self.about_us, image=self.bgpicabt)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.G.pack()

	def on_submit_carddetails(self):
		"""This function is executed when the submit button on the add card page is pressed.
		This function gets all the details entered in the entry boxes created in the add card page and passes all the details to a
		funtion which adds all those details to the database."""

		#The data entered in entry boxes is collected using get funtion and stored in respective variables.
		self.card_holder_name1=self.e8.get()
		self.card_number1=self.e9.get()
		self.expiry_month1=self.e10.get()
		self.expiry_year1=self.e11.get()
		self.cvv1=self.e12.get()

		#The data in the variables is passed to the function which updates the details in database.
		self.card(self.card_holder_name1,self.card_number1,self.expiry_month1,self.expiry_year1,self.cvv1)

		#This function destroys the add card page and takes the user to options page.
		self.add.destroy()

	def mobile_recharge(self):
		"""
		This function eliminates the need for performing mouse clicks and keypresses manually,
		which are required to carry out mobile recharge, and runs the whole process automatically.
		"""

		# Import the necessary libraries.
		import pyautogui,time

		# Open 'Google Chrome' after the command from the user.
		pyautogui.press('win')
		pyautogui.typewrite('Google Chrome',0.01)
		pyautogui.press('enter')

		# Give a delay for about 5 sec, to make the system open Google Chrome.
		time.sleep(5)

		# To maximize the new tab window which will be opened on the screen, after the delay.
		pyautogui.hotkey('alt','space')
		pyautogui.press('x')

		# Place the cursor into the URL bar to start typing the link.
		pyautogui.click(151,51)
		pyautogui.typewrite('https://www.airtel.in/prepaid-recharge?icid=prepaid_row_1_column_1')
		pyautogui.press('enter')

		# Give a delay for about 10 seconds to open the mentioned webpage.
		time.sleep(10)

		# Click on the coordinates of the last digit of the mobile number in the space provided to type the number. 
		pyautogui.click(772,269)

		# Erase the already pre-taken number if any.
		for i in range(10):
			pyautogui.press('backspace')

		# Type the 'Mobile number' of the user in the erased space,followed by required amount of delay.
		numb1=self.ph(self.usernameinp)
		pyautogui.typewrite(numb1,0.01)
		time.sleep(10)

		# Type the 'Amount of recharge' to be done, followed by required amount of delay.
		pyautogui.typewrite('35')
		time.sleep(5)

		# Press 'Enter' key to activate Recharge and proceed to payment, followed by required amount of delay.
		pyautogui.press('enter')
		time.sleep(20)

		# First click on 'Debit/Credit Card' option to fill the card details
		pyautogui.click(100,475)

		# Function call to retrieve and type the card holder's name from the database.
		chn1=self.c_h_n()
		time.sleep(1)
		pyautogui.click(350,338); pyautogui.typewrite(chn1,0.01)

		# Function call to retrieve card number from the database.
		cn1=self.c_n()
		pyautogui.click(300,430); pyautogui.typewrite(cn1,0.01)
		
		# Function call to retrieve and type the month of expiry of the card from the database.
		expm2=self.expm()
		pyautogui.click(705,430); pyautogui.typewrite(expm2,0.01)

		# Function call to retrieve and type the year of expiry of the card from the database.
		expy2=self.expy()
		pyautogui.click(750,430); pyautogui.typewrite(expy2,0.01)

		# Function call to retrieve and type the CVV of the card from the database.
		cvv2=self.c_v_v()
		pyautogui.click(830,430); pyautogui.typewrite(cvv2,0.01)

		# Click on 'Continue to pay' option to receive an OTP to the associated number and to complete the payment.
		pyautogui.click(1000,600)

	def dth_recharge(self):
		"""
		This function eliminates the need for performing mouse clicks and keypresses manually,
		which are required to carry out DTH recharge, and runs the whole process automatically.
		"""

		# Import the necessary libraries.
		import pyautogui,time
		# Open 'Google Chrome' after the command from the user.
		pyautogui.press('win')
		pyautogui.typewrite('Google Chrome')
		pyautogui.typewrite(['enter'])

		# Give a delay for about 5 sec, to make the system open Google Chrome.
		time.sleep(5)

		# To maximize the new tab window which will be opened on the screen, after the delay.
		pyautogui.hotkey('alt','space')
		pyautogui.press(['x'])

		# Place the cursor into the URL bar to start typing the link.
		pyautogui.click(151,51)
		pyautogui.typewrite('https://www.tatasky.com/wps/portal/TataSky/help/recharge-online')
		pyautogui.typewrite(['enter'])

		# Give a delay for about 10 seconds to open the mentioned webpage.
		time.sleep(10)

		# Click on the Quick Recharge option on the screen, followed by a delay, to carry out the recharge.
		pyautogui.click(1119,120)
		time.sleep(2)

		# Perform scroll operation twice to view the textboxes available on the screen, to fill the details.
		pyautogui.press(['down'])
		pyautogui.press(['down'])

		# To perform a click on the first textbox on the screen, to enter the mobile number.
		pyautogui.click(720,470)
		pyautogui.typewrite('9945990000',0.01)

		# To perform a click on the second textbox on the screen, to enter the recharge amount.
		pyautogui.click(618,592)
		pyautogui.typewrite('3175',0.01)

		# Click on the 'Pay Now' option after a delay of 2 seconds.
		time.sleep(2)
		pyautogui.click(665,682)

		# Give a delay for about 10 seconds to load the type of payment page.
		time.sleep(10)

		# To click on the 'Debit card' option followed by clicking on 'Pay Now'.
		pyautogui.click(330,405)
		pyautogui.click(1150,543)

		# Give a delay of 10 seconds to load the next Payment page.
		time.sleep(10)

		# Click on Debit card, followed by 'Select' option on the screen to select what type of debit card.
		pyautogui.click(681,375)
		pyautogui.click(959,413)

		# Click on 'Rupay Card' option from the drop down occured. 
		pyautogui.click(864,579)

		# Click on 'Pay Now' option.
		pyautogui.click(805,465)

		# Give a delay for about 5 seconds to load the card details page.
		time.sleep(5)

		# Click on the first textbox on the screen to enter the card number.  
		pyautogui.click(620,445)

		# Function call to retrieve and type the card number from the database.
		cn1=self.c_n()
		pyautogui.typewrite(cn1,0.01)

		# Function call to retrieve and type the card holder's name from the database.
		chn1=self.c_h_n()
		pyautogui.click(620,479); pyautogui.typewrite(chn1,0.01)

		# Function call to retrieve and type the month of expiry of the card from the database.
		expm2=self.expm()
		pyautogui.click(552,512); pyautogui.typewrite(expm2,0.01)

		# Function call to retrieve and type the year of expiry of the card from the database.
		expy2=self.expy()
		expy3="20"+expy2
		pyautogui.click(606,513); pyautogui.typewrite(expy3,0.01)

		# Function call to retrieve and type the CVV of the card from the database.
		cvv2=self.c_v_v()
		pyautogui.click(550,550); pyautogui.typewrite(cvv2,0.01)

		# Click on final 'Pay Now' option to proceed to enter the OTP received.
		pyautogui.click(373,634)


	# This function is used for signing up of the user to the easy_pay database
	def signup(self,f_firstname, f_lastname, f_email_id ,f_phone_no ,f_username ,f_password):
		# The arguments are taken into variables such as firstname, lastname, email id ,phone number,username and password for future use
		self.firstname = f_firstname
		self.lastname = f_lastname
		self.email_id = f_email_id
		self.phone_no = f_phone_no
		self.username = f_username
		self.password = f_password
		''' In the following part of code of this function, we use try block to create a row in database or if it 
    	 already exists then except block is used to update the row'''
		print("Created New Sign Up")
		try:
			print("creating")
			Customer.create(first_name = self.firstname, last_name = self.lastname, email_id = self.email_id ,phone_number = self.phone_no, user_name = self.username, password = self.password)
		except:
			print("updating")
			Customer.update(first_name = self.firstname, last_name = self.lastname, email_id = self.email_id ,phone_number = self.phone_no, user_name = self.username, password = self.password)
		print("updated to db")


	# This function is used to login to easypay
	def login(self,f_username, f_password):
		# passing arguments into respective variables for future use
		self.username = f_username
		self.password = f_password

		try:
			# query1 is the variable which selects the username column's values
			query1 = Customer.select().where(Customer.user_name == self.username)
			# now to check the password and username that has been passed to the function is same as the username and password that is present in the database
			if ((self.password == query1[0].password) and (query1[0].user_name == self.username)):
				return True
			else:
				return False

		except:
			return False


	# This function is used to retrieve phone number from the customer table of database
	def ph(self,f_username):
		self.username = f_username
		# By taking usernsme as reference to get the phone number of the customer from customer table 
		query2= Customer.select().where(Customer.user_name == self.username)
		self.ph_no = query2[0].phone_number
		# Returning the phone number
		return self.ph_no
	
	
	# This function is used to add the card details to the card details table of the database
	def card(self,f_card_holder,f_card_no,f_exp_month,f_exp_year,f_cvv):
		# passing arguments into respective variables for future use
		self.card_holder_name1 = f_card_holder
		self.card_number1 = f_card_no
		self.expiry_month1 = f_exp_month
		self.expiry_year1 = f_exp_year
		self.cvv1 = f_cvv
		# Adding the card details of the customer
		Card_details.create(card_holder_name = self.card_holder_name1, card_number = self.card_number1, expiry_month = self.expiry_month1 ,expiry_year = self.expiry_year1 , cvv = self.cvv1)


	# This function is used to retrieve the card holder name from database 
	def c_h_n(self):
		# The following query searches for the card holder name in the card details table
		query3= Card_details.select().where(Card_details.customer==1)
		self.chn = query3[0].card_holder_name
		# Returning the card holder name 
		return self.chn
	

	# This function is used to retrieve the card number from the database 
	def c_n(self):
		# The following query searches for the card number in the card details table
		query4= Card_details.select().where(Card_details.customer==1)
		self.cn = query4[0].card_number
		# Returning the card number
		return self.cn
	

	# This function is used to retrieve the expiry month of the card from the database 
	def expm(self):
		# The following query searches for the expiry month in the card details table
		query5= Card_details.select().where(Card_details.customer==1)
		self.expm1 = query5[0].expiry_month
		# Returning the card expiry month
		return self.expm1
	

	# This function is used to retrieve the expiry year of the card from the database 
	def expy(self):
		# The following query searches for the expiry year in the card details table
		query6= Card_details.select().where(Card_details.customer==1)
		self.expy1 = query6[0].expiry_year
		# Returning the card expiry year
		return self.expy1


	# This function is used to retrieve the cvv of the card from the database 
	def c_v_v(self):
		# The following query searches for the cvv in the card details table
		query7= Card_details.select().where(Card_details.customer==1)
		self.cvvn= query7[0].cvv
		# Returning the cvv
		return self.cvvn

"""EasyPayApp class is called on an object 'app' and mainloop function is run on it"""
app = EasyPayApp()
app.mainloop()