


def convert(number):
    """Converts hexidecimal strings into binary

    Args:
        number (string): Should be hexadecimal

    Returns:
        String: Binary form of inputted hexadecimal string
    """
    table = {'0':'0000', '1':'0001', '2':'0010',
             '3':'0011', '4':'0100', '5':'0101',
             '6':'0110', '7':'0111', '8':'1000',
             '9':'1001', 'A':'1010', 'B':'1011',
             'C':'1100', 'D':'1101', 'E':'1110',
             'F':'1111'}
    binary = ""
    for digit in number:
        binary = table[digit] + binary
    return binary



def userInput(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = input(value)
    quitKey = "q"
    while True:
        if result == "q":
            print("Quiting script...")
            quit()
        else:
            return result