# https://adventofcode.com/2016

#? part 1
with open("data.txt", 'r') as f:
    instructions = f.readline()

l = instructions.split(", ")

blocks = 0

for step in l:
    match step[0]:
        case 'R':
            blocks += int(step[1])
        case 'U':
            blocks += int(step[1])
        case 'L':
            blocks -= int(step[1])
        case 'D':
            blocks -= int(step[1])
        case _:
            print("SOMETHING HAS GONE WRONG")

print(blocks)
