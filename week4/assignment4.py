# Create function to get user input and check for q
def userInput(value):
    result = input(value)
    if result == "q":
        exit()
    else:
        return result

# Start loop for script
while True:
    # Advise user how to quit
    print("At any point, enter 'q' to quit.")
    
    # Get user inputs
    name = userInput("Please enter your name or 'q' to quit: ")
    balance = float(userInput("Please enter your account balance: $"))
    n = float(userInput("Enter an amount to withdraw (-) or to deposit (+): $"))
    
    # Check if n is negative
    if n > 0:
        # Add n to balance
        balance = round(balance + n,2)
        
    elif n < 0:
        # Convert n to positive and subtract
        balance = round(balance - (n * -1),2)
        """
        Originally I just added n regardless since a negative added is the same 
        as subtracting a positive but assignment specifically says to subtract 
        if negative
        """
    
    # Display new account balance
    if balance > 0:
        print(f"Your new account balance is ${balance}")
    elif balance < 0:
        print(f"Your account is overdrawn by ${balance}.")
    else:
        print("Your account balance is zero")