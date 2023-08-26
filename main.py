my_name = input("enter your name:")
my_age = input("enter your age ")
print(f"my name is {my_name} and i am {my_age} years old")
first_number = int(input("enter the first number:"))
second_number = int(input("enter the second number:"))
operation = input("enter your operation:")
if operation == "+":
    print("first_number + second_number")
elif operation == "-":
    print("first_number - second_number")    
elif operation == "/":
    print("first_number / second_number")
elif operation == "*":
    print("first_number * second_number")
bus_capacity =  30   
peopleinbus = int(input("enter the amount of passengers inside the bus:"))
peoplewantbus = int(input("enter the amount of people that want to enter the bus:"))
empty_seats = bus_capacity - peopleinbus
if empty_seats > peoplewantbus
    print(f"there are {empty_seats} empty seats")
 else: print("the bus is full")
