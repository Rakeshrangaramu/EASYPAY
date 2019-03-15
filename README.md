# Easypay-An Automated Payment Application
Easypay is an automated payment application which is developed in order to automate the payments we do repeatedly in our day-to-day lives. Here we have considered an example of mobile and d2h recharge.

The application is developed based on Tkinter, Pyautogui and PeeWee.
Tkinter is used to design the frontend of the application, Pyautogui is used for automation process and PeeWee is used for creating and maintaining database.

Initially, after running the application, homepage appears in which the user is first prompted to signup inorder to use the application.
The details entered by the user in the signup page gets stored in the database.

Now user needs to login again with valid credentials as entered while signup. User needs to add their card details for first time usage by clicking on add card option.

After choosing the required option among the two recharges, further steps involved are performed automatically until the user gets the OTP on registered mobile number.
Here the user needs to manually enter the OTP which serves as security check incase of any unauthorized access.

## Running the application
Pre-requisites to run the application:

pip install pyautogui

pip install peewee

In a new folder, pull all the files in the repository and run the batchfile.bat

Carry out the process explained above.
