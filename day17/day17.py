print("homework")
def print_even_indices(name):
    for i in range(len(name)):
        if i % 2 == 0:
            print(name[i])

def main():
    full_name = input("Enter your first and last name: ")
    print("Pointers at even indices:")
    print_even_indices(full_name)

if __name__ == "__main__":
    main()










def check_for_5(numbers):
    if 5 in numbers:
        print("5, is in the list.")
    else:
        print("5, is not in the list.")
numbers_list = [1, 2, 3, 4, 6, 7, 8, 9]
check_for_5(numbers_list)
