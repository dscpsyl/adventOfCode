# https://adventofcode.com/2021

#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# prev = int(lines[0])
# lines.pop(0)

# inc = 0

# for l in lines:
#     if int(l) > prev:
#         inc += 1
#     prev = int(l)

# print(inc)

#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# inc = 0

# lines = [eval(o) for o in lines]

# combined = []

# for i, l in enumerate(lines):
#     if((i+1) == len(lines)-1):
#         break
#     combined.append(sum([l, lines[i+1], lines[i+2]]))


# prev = combined[0]
# combined.pop(0)

# for l in combined:
#     if l > prev:
#         inc += 1
#     prev = l

# print(inc)