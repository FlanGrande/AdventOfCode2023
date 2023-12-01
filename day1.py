import lib.puzzle as puzzle

numbers_as_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Read a string and build a dictionary of words and their positions
def find_words(string, direction = "forward"):
    words = {}
    for word in numbers_as_words:
        if word in string:
            if direction == "forward":
                word_pos = string.find(word)
            
            if direction == "backward":
                word_pos = string.rfind(word)

            words[word] = word_pos
    return words

# Return the word in the dictionary with the lowest position
def find_first_word(words):
    first_word = ""
    first_pos = 100000
    
    for word in words:
        if words[word] < first_pos:
            first_pos = words[word]
            first_word = {}
            first_word[word] = first_pos
    
    return first_word

# Return the word in the dictionary with the highest position
def find_last_word(words):
    last_word = ""
    last_pos = -1
    
    for word in words:
        if words[word] > last_pos:
            last_pos = words[word]
            last_word = {}
            last_word[word] = last_pos
    
    return last_word

def convert_word_to_digit(word):
    if word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9
    else:
        return int(word)

puzzle_input = puzzle.read_puzzle_input_as_lines('puzzle_inputs/day1.txt')
solution = 0

count = 0

for line in puzzle_input:
    count += 1
    words_forward = find_words(line, "forward")
    words_backwards = find_words(line, "backward")
    first_word = find_first_word(words_forward)
    last_word = find_last_word(words_backwards)

    #first_word_pos = list(first_word.values())[0]
    #last_word_pos = list(last_word.values())[0]

    first_word = list(first_word.keys())[0]
    last_word = list(last_word.keys())[0]
    
    first_digit = convert_word_to_digit(first_word)
    last_digit = convert_word_to_digit(last_word)
    solution += first_digit*10 + last_digit
    
    #print("Line " + str(count) + ": " + line)
    #print("First word: " + first_word + " at position " + str(first_word_pos))
    #print("Last word: " + last_word + " at position " + str(last_word_pos))

    #print("")



print(solution)