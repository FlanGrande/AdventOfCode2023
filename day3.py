import lib.puzzle as puzzle
import pandas as pd
import numpy as np

puzzle_input = np.array(puzzle.read_puzzle_input_as_matrix('puzzle_inputs/day3_sample.txt'))
puzzle_shape = np.shape(puzzle_input)
symbols = "*-%/#&$=@+!?"
solution_part_1 = 0
solution_part_2 = 0

print(puzzle_input)
print(puzzle_shape)

def is_inside_puzzle(i, j):
    return i >= 0 and i < puzzle_shape[0] and j >= 0 and j < puzzle_shape[1]

def is_symbol(char):
    if char in symbols:
        return True
    else:
        return False

def get_neighbour(i, j):
    if not is_inside_puzzle(i, j):
        value = "-1"
    else:
        value = puzzle_input[i][j]

    return (i, j, value)

def get_neighbours(i, j):
    neighbours = []

    neighbours.append(get_neighbour(i - 1, j - 1))
    neighbours.append(get_neighbour(i - 1, j))
    neighbours.append(get_neighbour(i - 1, j + 1))
    neighbours.append(get_neighbour(i, j - 1))
    neighbours.append(get_neighbour(i, j + 1))
    neighbours.append(get_neighbour(i + 1, j - 1))
    neighbours.append(get_neighbour(i + 1, j))
    neighbours.append(get_neighbour(i + 1, j + 1))

    return (neighbours)

def get_left_neighbour(i, j):
    return get_neighbour(i, j - 1)

def get_right_neighbour(i, j):
    return get_neighbour(i, j + 1)

def build_numbers_dict():
    numbers = {}

    for i in range(puzzle_shape[0]):
        building_number = False
        number = ""

        for j in range(puzzle_shape[1]):
            current_char = puzzle_input[i][j]
            if current_char.isdigit():
                if not building_number:
                    building_number = True
                    number = current_char
                else:
                    number += current_char
            else:
                if building_number:
                    numbers[(i, j - 1)] = int(number)
                    building_number = False
                    number = ""
        
        if building_number:
            numbers[(i, j - 1)] = int(number)
            building_number = False
            number = ""
    
    return numbers


def is_number_a_part_of_the_machine_part_1(position):
    is_part_of_machine = False

    neighbours = get_neighbours(position[0], position[1])

    for neighbour in neighbours:
        if is_symbol(neighbour[2]):
            return True
    
    if is_inside_puzzle(position[0], position[1]):
        left_neighbour = get_left_neighbour(position[0], position[1])

        if left_neighbour[2] != ".":
            is_part_of_machine = is_number_a_part_of_the_machine_part_1(left_neighbour)
    
    return is_part_of_machine

print()

def get_valid_gears_part_2():
    valid_gears = []

    for i in range(puzzle_shape[0]):
        for j in range(puzzle_shape[1]):
            candidate = get_neighbour(i, j)
            
            if is_inside_puzzle(candidate[0], candidate[1]):
                if candidate[2] == "*":
                    if not candidate in valid_gears:
                        valid_gears.append(candidate)
    
    return valid_gears

numbers = build_numbers_dict()

for number in numbers:
    is_part = is_number_a_part_of_the_machine_part_1(number)
    #print(number, numbers[number], is_part)
    if is_part:
        solution_part_1 += numbers[number]

print(solution_part_1)

valid_gears = get_valid_gears_part_2()

print(valid_gears)
print()

def is_number_adjacent_to_a_valid_gear(number):
    is_adjacent = False

    for j in range(puzzle_shape[1]):
        candidate = get_neighbour(number[0], j)
        if candidate in valid_gears:
            return True

    neighbours = get_neighbours(number[0], number[1])

    for neighbour in neighbours:
        if neighbour in valid_gears:
            return True
    
    return is_adjacent

for number in numbers:
    if number in valid_gears:
        solution_part_2 += numbers[number]