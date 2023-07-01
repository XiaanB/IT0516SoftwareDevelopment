# Creating a function to convert currency  to or from a value
def conversion(how_much, conversioin_rate):
    answer = 0
    to_or_from = input("Would you like to convert from or to? (from/to)  ")
    if to_or_from == "to":
        answer = how_much * conversioin_rate
    else:
        answer = how_much / conversioin_rate
    return answer
   
    
# Creating 2 variables to store the user selections
how_much_nzdollars = int(input("How much whould you like to conver?  "))
conversioin_rate_nzdollars = float(input("What is you conversion rate? "))

# Callling the conversion function and the user providing the amount and
# conversion rate as arguments
print(conversion(how_much_nzdollars, conversioin_rate_nzdollars))
