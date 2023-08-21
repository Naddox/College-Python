# Import module(s)
from time import sleep

# Define variables
transactions = []
hl = "─" * 29
menu = {'1.':'Add Transaction', '2.':'Delete Transaction',
        '3.':'Edit Transaction', '4.':'Display Transactions',
        '5.':'Exit the Program'}


def transCheck():
    """Function that checks if any values are contained in the list

    Returns:
        True when at least 1 value is in list
        False when list contains no values
    """
    _length = len(transactions)
    if _length >= 1:
        return True
    else:
        return False


def addTrans():
    """Allows user to add a new transaction to the transaction variable.
    If user enters nothing and presses enter, assumes user did not want
    to add a transaction and escape back to main menu.
    """
    while True:
        print("\nEnter transaction to add:")
        userInput = input()
        
        if userInput == "":
            # User entered no value, return to main menu
            print("No input detected. Returning to main menu...")
        else:
            # Add input to transactions list
            print(f"\nAdding {userInput} to transactions.")
            transactions.append(userInput)
            
        print("\nWould you like to add another transaction? (Yes / No)")
        userInput = input().lower()
        
        if userInput == "yes":
            # Restart loop
            pass
        else:
            # Return to main menu
            print("Loading main menu, please wait...")
            sleep(1)
            return
    
def delTrans():
    """Removes user selections from current transactions list by allowing user to selection which transaction
    to remove via index in list. Allows user to remove multiple transactions without returning to main menu
    between operations.
    """
    while transCheck():
        # Verify there are transactions to remove and prompt for user input.
        
        dispTrans(1)
        print(f"{hl}\nPlease select from the below options:")
        print(f"{hl}\n1-{len(transactions)} ─ Remove selected transaction")
        print("0 ─ Return to main menu")
        print("-1 ─ Clear all transactions")
        userInput = int(input())
        userInput -= 1
        length = len(transactions)
            
        
        if userInput in range(0, length):
            # Verify user input is a valid index of the transactions list.
            print(f"\nRemoving transaction {transactions[userInput]}...")
            transactions.pop(userInput)
            sleep(1)
            
            
        elif userInput == -1:
            # Return to main menu when user enters 0.
            print("Loading main menu, please wait...")
            sleep(1)
            return
        elif userInput == -2:
            # Clear all values in list.
            transactions.clear()
            print("All transactions cleared.")
        else:
            # Input was not in range and not 0, return to main menu
            print("Selection is invalid, returning to main menu...")
            sleep(1)
            return
        
        if transCheck():
            # Ask user if they want to remove more transactions
            print("Transaction removed...\nWould you like to remove another transaction? (Yes / No)")
            userInput = input().lower()
            if userInput == "yes":
                # Restart loop
                pass
            else:
                # Return to main menu
                print("Loading main menu, please wait...")
                sleep(1)
                return
        else:
            # No values remain to delete
            print("Last remaining transaction removed...\nReturning to main menu...")
            sleep(1)
            return
        
    # Return to main menu when no transactions exist.
    print("\nThere are no transactions to remove, returning to main menu...")
    sleep(1)
    return
    
def editTrans():
    while transCheck():
        # Verify there are values to edit.
        length = len(transactions)
        dispTrans(1)
        print(f"\nPlease select which transaction to edit by entering 1-{len(transactions)}, or enter '0' to return to the menu.")
        userInput = int(input())
        userInput -= 1
        
        if userInput in range(0, length):
            # Update vlaue to users new value
            print(f"You selected {transactions[userInput]}, please enter its new value...")
            transactions[userInput] = input()
            print("\nUpdating transaction...")
            sleep(1)
            print(f"\nTransaction updated successfully to {transactions[userInput]}.")
            
        elif userInput == -1:
            # Return to main menu when user enters 0.
            print("Loading main menu, please wait...")
            sleep(1)
            return
        
        else:
            # Input was not in range and not 0, return to main menu
            print("Selection is invalid, returning to main menu...")
            sleep(1)
            return
        
        # Ask user if they want to remove more transactions
        print("\nWould you like to edit another transaction? (Yes / No)")
        userInput = input().lower()
        
        if userInput == "yes":
            # Restart loop
            pass
        else:
            # Return to main menu
            print("Loading main menu, please wait...")
            sleep(1)
            return
        
    # Return to main menu when no transactions exist.
    print("\nThere are no transactions to edit, returning to main menu...")
    sleep(1)
    return

def dispTrans(n=0):
    """Displays all current transactions in order with their index +1.
    Takes an optional argument for when being called by other functions"""
    
    if transCheck() == True:
        # Verify there are values to display and display them.
        print("\nDisplaying current transactions\n")
        
        for (i, item) in enumerate(transactions, start=1):
            # Print out each value in list next to their index + 1
            print(i, item)
    else:
        print("\nSuch empty, much wow...")
    
    if n == 0:
        # If n is not 0, it was called by another function and does not run these lines
        input("\nPress Enter to continue...")
        print("Loading main menu, please wait...")
        sleep(1)

def menuDisp():
    # Display menu
    print(f"\n{hl}\n**********Main Menu**********")
    for key in menu:
        print(key, menu[key])
    print(hl)
    print("\nChoose a menu option from 1-4 or 5 to exit the program:")
    select = input()
    
    # Get menu selection
    match select:
        case '1':
            addTrans()
        case '2':
            delTrans()
        case '3':
            editTrans()
        case '4':
            dispTrans()
        case '5':
            print("\nQuiting program...")
            quit()
            
def main():
    menuDisp()
    
if __name__ == "__main__":
    while True:
        main()