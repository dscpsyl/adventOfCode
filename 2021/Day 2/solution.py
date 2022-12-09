
#? Part 1

# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# lines = [l.split() for l in lines]

# foward = 0
# depth = 0

# for l in lines:
#     match l[0]:
#         case "forward":
#             foward += int(l[1])
#         case "up":
#             depth -= int(l[1])
#         case "down":
#             depth += int(l[1])
#         case _:
#             print(f"SOMETHING HAS GONE WRONG")
            

# print(foward * depth)


#? part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# lines = [l.split() for l in lines]

# foward = 0
# depth = 0
# aim = 0

# for l in lines:
#     match l[0]:
#         case "forward":
#             foward += int(l[1])
#             depth += (aim * int(l[1]))
#         case "up":
#             aim -= int(l[1])
#         case "down":
#             aim += int(l[1])
#         case _:
#             print(f"SOMETHING HAS GONE WRONG")
            

# print(foward * depth)