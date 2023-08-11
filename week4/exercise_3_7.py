# Gather the user inputs
startSalary = float(input("Enter the starting salary: $"))
rate = int(input("Enter the annual percentage increase: "))
years = int(input("Enter the number of years: "))

# Convert the rate to a decimal
rate = rate / 100

# Initialize raise accumulator
totalRaise = 0.0

# Display table header
print("%4s%10s" % \
    ("Year","Salary"))

# Seperate header from data
print("-----------------")

# Compute & display data for each year
for year in range(1, years + 1):
    _raise = startSalary * rate
    endSalary = startSalary + _raise
    print("%3d%12.2f" % \
        (year, startSalary))
    
    # Save raise to current salary
    startSalary = endSalary
    totalRaise += _raise
