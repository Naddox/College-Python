transactions = [1,2,3]

def transCheck():
    """Function that checks if any values are contained in the list

    Returns:
        True when at least 1 value is in list
        False when list contains no values
    """
    if any(transactions):
        return True
    else:
        return False
    


print(transCheck())