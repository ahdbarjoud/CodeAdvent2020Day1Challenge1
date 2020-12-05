def find_2020(numbers: list, target: int) -> int:
    for i, number in enumerate(numbers[:-1]):
        second_number = target - number
        if second_number in numbers[i+1:]:
            return number*second_number

with open("./input.txt", "r") as f:
    number_list = f.readlines()

target_number = 2020

print(find_2020([int(n) for n in number_list], target_number))
