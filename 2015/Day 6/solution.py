
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f.readlines()]


# for i, l in enumerate(lines):
#     temp = l.split(" ")
#     if temp[0] == "turn":
#         temp = temp[1:]
    
#     temp = temp[:2] + temp[3:]
    
#     temp[1] = temp[1].split(",")
#     temp[2] = temp[2].split(",")
    
#     lines[i] = temp

# lights = [[False for i in range(1000)] for j in range(1000)]

# for l in lines:
#     match l[0]:
#         case "on":
#             for i in range(int(l[1][0]), int(l[2][0])+1):
#                 for j in range(int(l[1][1]), int(l[2][1])+1):
#                     lights[i][j] = True
#         case "off":
#             for i in range(int(l[1][0]), int(l[2][0])+1):
#                 for j in range(int(l[1][1]), int(l[2][1])+1):
#                     lights[i][j] = False
#         case "toggle":
#             for i in range(int(l[1][0]), int(l[2][0])+1):
#                 for j in range(int(l[1][1]), int(l[2][1])+1):
#                     if lights[i][j]:
#                         lights[i][j] = False
#                     else:
#                         lights[i][j] = True
#         case _:
#             print(f"SOMETHING IS WRONG")
            
            
# on = 0            
# for i in lights:
#     for j in i:
#         if j:
#             on += 1
        
# print(on)

#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f.readlines()]


# for i, l in enumerate(lines):
#     temp = l.split(" ")
#     if temp[0] == "turn":
#         temp = temp[1:]
    
#     temp = temp[:2] + temp[3:]
    
#     temp[1] = temp[1].split(",")
#     temp[2] = temp[2].split(",")
    
#     lines[i] = temp

# lights = [[0 for i in range(1000)] for j in range(1000)]

# for l in lines:
#     match l[0]:
#         case "on":
#             for i in range(int(l[1][0]), int(l[2][0])+1):
#                 for j in range(int(l[1][1]), int(l[2][1])+1):
#                     lights[i][j] += 1
#         case "off":
#             for i in range(int(l[1][0]), int(l[2][0])+1):
#                 for j in range(int(l[1][1]), int(l[2][1])+1):
#                     if lights[i][j] != 0:
#                         lights[i][j] -= 1
#         case "toggle":
#             for i in range(int(l[1][0]), int(l[2][0])+1):
#                 for j in range(int(l[1][1]), int(l[2][1])+1):
#                     lights[i][j] += 2
#         case _:
#             print(f"SOMETHING IS WRONG")
            
            
# on = 0            
# for i in lights:
#     for j in i:
#         on += j
        
# print(on)