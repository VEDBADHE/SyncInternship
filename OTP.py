#importing necessary libraries
import os
import math
import random
import smtplib

#Generating OTP
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp

#Conntecting server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
password='rmxdcjxhyljqepqa'
s.login("vedantbadhe76@gmail.com", password)

#taking userinput for email
emailid = input("Enter your email: ") 
s.sendmail('vedantbadhe76@gmail.com','vedantbadhe762@gmail.com',msg)

#taking userinput for OTP
a = input("Enter Your OTP >>: ") 
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")