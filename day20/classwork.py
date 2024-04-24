#davaleba (1)
def sum_of_two_min(numbers):
    sorted_numbers = sorted(numbers)
    
    return sorted_numbers[0] + sorted_numbers[1]

test_cases = [
    ([5, 8, 12, 18, 22], 13),
    ([7, 15, 12, 18, 22], 19),
    ([25, 42, 12, 18, 22], 30)
]
for numbers, expected_sum in test_cases:
    result = sum_of_two_min(numbers)
    print(f"For {numbers}, expected sum: {expected_sum}, actual sum: {result}")


#davaleba (2)
def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

test_cases = [
    ([1, 2, 3, 4], [2, 4])
]

for numbers, expected_result in test_cases:
    result = filter_even_numbers(numbers)
    print(f"For {numbers}, expected result: {expected_result}, actual result: {result}")



def calculate_points(list1, list2):
    points = 0
    
    for item1, item2 in zip(list1, list2):
        if item1 == "" or item2 == "":
            continue
        
        if item1 == item2:
            points += 4
        else:
            points -= 1
    
    return points

test_cases = [
    (["a", "a", "b", "b"], ["a", "c", "b", "d"]), #(1)unda amovides
    (["a", "a", "c", "b"], ["a", "a", "b", ""]),  #(10)unda amovides
    (["a", "a", "b", "c"], ["a", "a", "b", "c"]), #(16)unda amovides
    (["b", "c", "b", "a"], ["", "a", "a", "c"])   #(-3)unda amovides
]

for list1, list2 in test_cases:
    points = calculate_points(list1, list2)
    print(f"For lists {list1} and {list2}, points: {points}")



#davaleba(4)
def sum_even_odd_indices(numbers):
    sum_even = sum(numbers[i] for i in range(len(numbers)) if i % 2 == 0)
    sum_odd = sum(numbers[i] for i in range(len(numbers)) if i % 2 != 0)
    return [sum_even, sum_odd]

test_cases = [
    ([80], [80, 0]),
    ([100.50], [100.50]),
    ([50, 60, 70, 80], [120, 140]),
    ([13, 27, 49], [62, 27]),
    ([70, 58, 75, 34, 91], [236, 92])
]

for numbers, expected_result in test_cases:
    result = sum_even_odd_indices(numbers)
    print(f"For {numbers}, expected result: {expected_result}, actual result: {result}")









