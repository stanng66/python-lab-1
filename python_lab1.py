# ====================
# Lab 1
# Stanley Nguyen (N01570766)
# Humber College
# CPAN-214-RNA
# Naresh Sirwani
# September 22, 2026
# --------------------
# This program practices Datatypes
# ====================
# Task 1: Create variable named x and assign value = 4
x = 4

# Task 2: Create variable named y and assign value = 2
y = 2

# Task 3: Print x + y
print (x + y)

# Task 4: Create a variable named car_name and assign value “Mercedes”
car_name = "Mercedes"

# Task 5: Create a variable named num_wheels and assign value of 4
num_wheels = 4

# Task 6: Print f-string with car_name and num_wheels
print (f"The car brand is {car_name} and it has {num_wheels} wheels")

# Task 7: Create variable named name and assign value of your name
name = "Stanley"

# Task 8: Create variable named num_apples and assign value of 24
num_apples = 24

# Task 9: Create variable named num_friends and assign value of 7
num_friends = 7

# Task 10: Print f-string with name, num_apples, num_friends, and apples_per_friend
apples_per_friend = num_apples / num_friends

print (f"{name} has {num_apples} apples and {num_friends} friends. Each friend gets {apples_per_friend:.2f} apples.")

# Task 11: Create variable named bill total and assign value of 120
bill_total = 120

# Task 12: Print f-string with num_people, bill_total, and cost_per_person formatted to 2 decimal places
num_people = 5
cost_per_person = bill_total / num_people

print (f"The bill total is ${bill_total:.2f} and there are {num_people} people. Each person pays ${cost_per_person:.2f}.")

# Task 13: Print f-string with num_people, bill_total, and cost_per_person formatted to an int
print (f"The bill total is ${bill_total} and there are {num_people} people. Each person pays ${int(cost_per_person)}.")

# Task 14: Create variable named dessert_cost and assign value = 6.55
dessert_cost = 6.55

# Task 15: Print f-string with num_people, dessert_cost, and total_cost_of_desserts formatted to 2 decimal places
total_cost_of_desserts = dessert_cost * num_people
print (f"The desert cost is ${dessert_cost:.2f} and there are {num_people} people. The total cost of dessert is ${total_cost_of_desserts:.2f}.")