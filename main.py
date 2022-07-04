#Your Life In Weeks 

age = input("what is yout current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int 
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(months_remaining)

message = f"you have {days_remaining} days,{weeks_remaining} weeks, and {months_remaining} months left"
print(message) 


#How to 
#1. Changing age into a number by using a string data type and inorder to do math we have to do a type conversion

#age will never be a float, because nobody is going to tell you they are 20.433 years old only whole numbers 

# age as a int (age)
# We have to caculate the number of years left 
#call it years remaining and guesswe are living to 90 and then -  age as a int 

#we gototta caculate weeks months and days \
#caculate number of years remaining and the age as a interger 

# now caculate days weeks and months left