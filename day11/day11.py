print("davaleba1")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

print("davaleba2")
for i in range(2, 21):
    if i % 2 == 0:
        print(i)
    
print("davaleba3")
nummer1 = 5
nummer2 = 11
x = 1
for i in range(nummer1,nummer2):
    print(i)
    x = x * i
print(x) 

print("davaleba4")
val = input("Enter a number: ")
if val.isnumeric():
    val = int(val) 
    x = 1
    for i in range(1, val + 1):
        x = x * i
    print(x)
else: print("the number must be a positive integer")


print("davaleba5")

try:
    number = float(input("Enter a number: "))
except ValueError:
    print("number is not valid")
else:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)



print("davaleba6")
number = 10

while number > 0:
    print(number)
    number -= 1

print("davaleba7")
name = input('Enter your name, or type quit to exit ')
keep_going = True
while keep_going:
    if name == "quit":
        keep_going = False

print("davaleba8")
number = 10
while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 2

print("davaleba9")
while True:
    try:
        number = float(input("Enter a number (positive): "))
        if number > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


print("davaleba10")
number = 1
while number <= 10:
    print(number, "\t",number ** 2)
    number += 1
