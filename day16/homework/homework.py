print("homework")

name_list = ["mateo","nino","josi","rosa","robert","lali"]
print(name_list[0], name_list[1],name_list[2],name_list[3],name_list[4],name_list[5])



number_list = ["1", "2","3","4","5","6","7","8","9","10"]
print(number_list[0],number_list[1],number_list[2],number_list[3],number_list[4],number_list[5],number_list[6], number_list[7],number_list[8],number_list[9],number_list[10])



numbers = list(range(10, 21))
for i in range(0, len(numbers), 2):
    numbers[i] = 1
print(numbers)




name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
place_of_residence = input("Enter your place of residence: ")
email = input("Enter your email: ")

user_info = [name, last_name, age, place_of_residence, email]

print("User information:")
print("Name:", user_info[0])
print("Last Name:", user_info[1])
print("Age:", user_info[2])
print("Place of Residence:", user_info[3])
print("Email:", user_info[4])


word = "no school"

print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[6])
print(word[7])
print(word[8])
print(word[9])
