# Import modules
import array as arr
import random

# Create array for float values
_amount = arr.array('d',[])

# Prompt user for their name
_name = input("Please enter your name : ").capitalize()

# Prompt user for amounts
while len(_amount) != 5:
_amount.append(float(input("Please enter an amount : ")))

# Get the sum of all amounts
_sum = round(sum(_amount),1)

# Create various different greetings
_greetings = [
    "Hello " + _name,
    "Good afternoon " + _name,
    "Good morning " + _name,
    "Good to see you again " + _name
]
# Select random greeting
_greet = random.choice(_greetings)

# Tell the user their balance
if _sum > 0:
    print(_greet + ", your account balance is $" + str(_sum))
elif _sum == 0:
    print(_greet + ", your account balance is zero")
elif _sum < 0:
    print(_greet + ", your account is currently overdrawn by :" + str(_sum))