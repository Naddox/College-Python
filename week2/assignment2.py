# Ask the user to enter a name, gross income, & state tax and save inputs to variables 
_name = input("Please enter your name: ")
_grossIncome = float(input("Please enter your gross income: "))
_stateTax = float(input("Please enter your state's tax rate: "))

# Calculate different tax rates
_fedTax = float(_grossIncome*0.0945)
_ficaTax = float(_grossIncome*0.0765)
_stTax = float(_grossIncome*(_stateTax*0.01))

# Calculate the estimated tax
_estTax = float(round(_stTax+_fedTax+_ficaTax,2))

# Printout
print(_name+"'s estimated tax is","$"+str(_estTax),"based on a gross income of","$"+str(_grossIncome))