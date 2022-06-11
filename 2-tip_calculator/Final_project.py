# Day 2 Final project
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill: $"))
tip_amount = int(input("What % tip you would like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

tip_with_bill = (tip_amount / 100) * total_bill + total_bill
bill_per_person = tip_with_bill / total_people
final_bill = round(bill_per_person, 2)
# method to round number to 2 decimal places
final_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_bill}")