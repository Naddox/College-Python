import math

def computer_guesses(smaller, larger):
    # Calculate the minimum number of guesses needed using log2
    min_guesses = math.ceil(math.log2(larger - smaller + 1))
    print("I will make no more than " + str(min_guesses) + " guesses.")

    # Initialize the guess count and set the initial range
    guess_count = 0
    low, high = smaller, larger

    while guess_count < min_guesses:
        # Make a guess and increment the guess count
        guess = (low + high) // 2
        guess_count += 1
        print("Your number is " + str(guess))
        
        # Ask the user for feedback
        feedback = input("Enter =, <, or >: ")

        if feedback == "=":
            print("Hooray, I've got it in " + str(guess_count) + " tries!")
            return
        elif feedback == "<":
            high = guess - 1
        elif feedback == ">":
            low = guess + 1
        else:
            print("Invalid input. Please enter =, <, or >.")

    print("I'm out of guesses, and you cheated!")

# Test the function
def main():
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    print(f"{smaller} {larger}")
    computer_guesses(smaller, larger)


main()
