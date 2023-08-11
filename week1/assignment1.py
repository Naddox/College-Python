
# Print out name of the file
print('Week 1 Assignment by Caleb Kopitzke')

# Ask for the users name and wish them a good day
name = input('Please enter your name: ')
print('Hello ' + name, ", I hope you're having a great day.")

# Prompt the user for valuex input and read back the input
valuex = float(input(name + ', please enter a value for X: '))
print('You entered a value of ', valuex, ' for X. Now we need a value for Y.')

# Prompt the user for the valuey input and back the input
valuey = float(input(name + ', please enter a value for Y: '))
print('You entered a value of ', valuey, ' for Y. Now we can add the two values together to get their sum.')

# Add together the inputs and assign to total and then print out both values and their sum
total = valuex + valuey
print('The sum of ', valuex, ' and ', valuey, ' is equal to ', total, '.')