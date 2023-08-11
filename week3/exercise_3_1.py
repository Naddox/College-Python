# Put your code here
ar = []

def check(list):
    return all(i == list[0] for i in list)

n = int(input("Please enter the first side : "))
ar.append(n)


n = int(input("Please enter the second side : "))
ar.append(n)


n = int(input("Please enter the third side : "))
ar.append(n)


x = check(ar)
print(x)

if x:
    print("The triangle is equilateral.")

else:
    print("The triangle is not equilateral.")
