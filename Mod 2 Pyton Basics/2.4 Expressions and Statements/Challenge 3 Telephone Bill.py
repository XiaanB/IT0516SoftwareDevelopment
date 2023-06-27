# 50 mins and 50txt for $15
#1min extra @ 0.25c
#1 txt @ 0.15c
# call centre charge = 0.44c
#Entire bill has a 5% sales tax

fix_charge = 15.0
extra_minutes = 25
extra_txt = 15
flat_rate = 0.44
sales_tax = 5/100

minutes_used_per_month = int(input("Please enter the number of minutes used this month: "))
txt_per_month = int(input("How many txt did you send this month? "))

if minutes_used_per_month > 50:
    minutes_used_per_month = (minutes_used_per_month - 50) * (extra_minutes/100)
    print("\n You will be charged and additional $", (round(minutes_used_per_month, 2)), "for using more than 50 mins")

if txt_per_month > 50:
    txt_per_month = (txt_per_month - 50) * (extra_txt/100)
    print("\nYou will be charged an additional $", (round(txt_per_month, 2)), "for using more than 50 txt's")

total_cost_before_tax = fix_charge + minutes_used_per_month + txt_per_month
total_cost_inlcuding_tax = (total_cost_before_tax * sales_tax) + total_cost_before_tax

print("\n\nYour base charge is:$", fix_charge)
print("Your 111 flat rate is $", flat_rate)



print("Your total bill before sales tax is: $", f'{(round(total_cost_before_tax, 2)):.2f}')
print("Your total bill before including a 5% sales tax is: $", (round(total_cost_inlcuding_tax, 2)))
