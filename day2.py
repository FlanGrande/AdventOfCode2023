import lib.puzzle as puzzle

puzzle_input = puzzle.read_puzzle_input_as_lines('puzzle_inputs/day2.txt')
games = {}
solution_part_1 = 0
solution_part_2 = 0

R_MAX = 12 # Red max cubes
G_MAX = 13 # Green max cubes
B_MAX = 14 # Blue max cubes

def get_game_id(line):
    game_id = line.split(":")[0]
    game_id = game_id.removeprefix("Game ")
    return int(game_id)

def print_game(game_id, sets):
    print(f"Game id: {game_id}")
    print(f"Set dict: {sets}")

def is_game_possible(sets):
    is_game_possible = True

    for set in sets:
        for cube in set:
            amount_shown = set[cube]

            match cube:
                case "red":
                    if amount_shown > R_MAX:
                        return False
                case "green":
                    if amount_shown > G_MAX:
                        return False
                case "blue":
                    if amount_shown > B_MAX:
                        return False
                case _:
                    print("Invalid color")
    
    return is_game_possible

def get_game_requirements(sets):
    red = 0
    green = 0
    blue = 0

    for set in sets:
        for cube in set:
            amount_shown = set[cube]

            match cube:
                case "red":
                    if amount_shown > red:
                        red = amount_shown
                case "green":
                    if amount_shown > green:
                        green = amount_shown
                case "blue":
                    if amount_shown > blue:
                        blue = amount_shown
                case _:
                    print("Invalid color")
    
    return (red, green, blue)

for line in puzzle_input:
    game_id = get_game_id(line)

    sets_of_revealed_cubes = line.split(":")[1].split(";")
    sets = []

    for set in sets_of_revealed_cubes:
        cubes = set.split(",")
        set_dict = {}

        for cube in cubes:
            cube = cube.strip()
            amount_shown = int(cube.split(" ")[0].strip())
            color = cube.split(" ")[1].strip()

            match color:
                case "red":
                    set_dict["red"] = amount_shown
                case "green":
                    set_dict["green"] = amount_shown
                case "blue":
                    set_dict["blue"] = amount_shown
                case _:
                    print("Invalid color")
        
        sets.append(set_dict)
    
    #print_game(game_id, sets)
    games[game_id] = sets

    if is_game_possible(games[game_id]):
        solution_part_1 += int(game_id)

for game in games:
    (red, green, blue) = get_game_requirements(games[game])
    solution_part_2 += red * green * blue

print(solution_part_1)
print(solution_part_2)