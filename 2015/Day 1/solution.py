
#? Part 1
# with open("data.txt", 'r') as f:
#     directions = f.readline()

# floor = 0

# for instruction in [*directions]:
#     print(instruction)
#     if instruction == "(":
#         floor += 1
#     else:
#         floor -= 1

# print(floor)

#? Part 2
# with open("data.txt", 'r') as f:
#     directions = f.readline()

# floor = 0
# position = 0

# for index, instruction in enumerate([*directions]):
#     if instruction == "(":
#         floor += 1
#     else:
#         floor -= 1
    
#     if floor == -1:
#         position = index+1
#         break

# print(position)