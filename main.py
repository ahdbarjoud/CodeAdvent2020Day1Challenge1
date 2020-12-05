from itertools import combinations
import math

def find_2020(numbers: list, target: int, combs: int) -> int:
    def validate(value):
        return sum(value) == target
    return math.prod(list(filter(validate, combinations(numbers, combs)))[0])

with open("./input.txt", "r") as f:
    number_list = f.readlines()

target_number = 2020

nums_to_use = 3

print(find_2020([int(n) for n in number_list], target_number, nums_to_use))
