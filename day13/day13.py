print("davaleba 3")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else: print(i)

print("davaleba 4")

try:
    number = float(input("Enter a number: "))
    if number > 0:
        print("the number you entered is positive")
    elif number < 0:
        print("the number you entered is negative.")
    elif number == 0:
        print("the number you entered is zero")
except ValueError:
    print("Invalid input. Please enter a number.")
    

print("davaleba 5")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)    

print("davaleba 6")
i = 1 
while i in range(1, 101):
    print(i)
    i += 1

print("davaleba7")
try:
    number = int(input("Enter a number: "))
    if number == 1:
        print("the number you entered is monday")
    elif number == 2:
        print("the number you entered is tuesday.")
    elif number == 3:
        print("the number you entered is wednesday")
    elif number == 4:
        print("the number you entered is thursday.")
    elif number == 5:
        print("the number you entered is friday")
    elif number == 6:
        print("the number you entered is saturday.")
    elif number == 7:
        print("the number you entered is sunday")    
    else: print("Invalid input. Please enter a number from 1-7.")
except ValueError:
    print("Invalid input. Please enter a number from 1-7.")


