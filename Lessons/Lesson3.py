print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do your want extra cheese? Y or N: ")

if size == "S" or "s":
    bill = 15
elif size == "M" or "m":
    bill = 20
else:
    bill = 25

if pepperoni == "Y" or "y":
    if size == "S" or "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y" or "Y":
    bill += 1

print(f"Your final bill is: ${bill}")