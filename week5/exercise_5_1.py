# Define imports
from collections import Counter

# Define functions
def median(lst):
    x = len(lst) # Get list length
    s = sorted(lst)
    if x == 0:
        return 0 # Return 0 when list contains nothing
    else:
        ind = x // 2 # Get the index of the list median
        if x % 2: # Determine if list contains odd or even number of values
            return s[ind] # Return for odd number
        else:
            return sum(s[ind-1:ind+1]) / 2 # Return for even numbers

def mode(lst):
    x = len(lst)
    dict = {} # Create dictionary
    
    if x == 0:
        return 0
    else:
        for num in lst:
            number = dict.get(num, None)
            if number == None: # First time number has appeared in list
                dict[num] = 1
            else:
                dict[num] = number + 1
        
        # Find the mode by finding which key appeared the most in the dictionary
        maximum = max(dict.values())
        for key in dict:
            if dict[key] == maximum:
                return key

def mean(lst):
    x = len(lst)
    
    if x == 0:
        return 0
    else:
        """Find & return the mean by adding all numbers in list together
            and deviding the sum by the count of numbers in list"""
        return sum(lst) / len(lst)
    
def main():
    # Set list of numbers
    list = [3,1,7,1,4,10]
    
    # Print result of functions
    print("Mode:", mode(list))
    print("Median:", median(list))
    print("Mean:", mean(list))



if __name__ == "__main__":
    main()
