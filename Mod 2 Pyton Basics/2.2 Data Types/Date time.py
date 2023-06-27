import datetime

import datetime as datetime
import datetime as timedelta
from datetime import datetime
from datetime import timedelta

date_input = input("Please enter your DOB in the format DD Mmm YYYY: \n")

date_object = datetime.strptime(date_input, '%d %b %Y')

print("The year you entered is: ", date_object.year, "\n")

my_age = datetime.today() - date_object
print(my_age)
print("My age in years is : ", my_age.days/365)