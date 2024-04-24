def main():
    elements = input("Enter elements separated by spaces: ").split()

    try:
        index = int(input("Enter an index: "))
        if 0 <= index < len(elements):
            print(f"The element at index {index} is: {elements[index]}")
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid index. Please enter a valid integer.")

if __name__ == "__main__":
    main()
