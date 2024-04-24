weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
index = input("Enter a number from 1-7 to return the corresponding weekday")
if index in ("1","2","3","4","5","6","7"):
    index = int(index) - 1
    print(weekdays[index])
else: print("Input not valid, enter a number from 1-7")