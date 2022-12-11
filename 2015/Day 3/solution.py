
#? Part 1
# with open("data.txt", 'r') as f:
#     line = f.readline()

# line = [*line]

# visited = {(0,0)}

# x = 0
# y = 0

# for l in line:
#     match l:
#         case "^":
#             y += 1
#         case ">":
#             x += 1
#         case "v":
#             y -= 1
#         case "<":
#             x -= 1
    
#     visited.add((x,y))

# print(len(visited))

#? Part 2
# with open("data.txt", 'r') as f:
#     line = f.readline()

# line = [*line]

# visited = {(0,0)}

# santa = True

# xSanta = 0
# ySanta = 0

# xRobo = 0
# yRobo = 0

# for i, l in enumerate(line):
#     if i % 2 == 0:
#         # then it's robo santa's turn
#         santa = False
#     else:
#         santa = True
        
#     match l:
#         case "^":
#             if santa:
#                 ySanta += 1
#             else:
#                 yRobo += 1
#         case ">":
#             if santa:
#                 xSanta += 1
#             else:
#                 xRobo += 1
#         case "v":
#             if santa:
#                 ySanta -= 1
#             else:
#                 yRobo -= 1
#         case "<":
#             if santa:
#                 xSanta -= 1
#             else:
#                 xRobo -= 1
                
    
#     visited.add((xSanta,ySanta))
#     visited.add((xRobo, yRobo))

# print(len(visited))