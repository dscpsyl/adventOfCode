
#? part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# x = 1
# y = 1

# numpad = { (0,0): 7, (0, 1): 4, (0, 2): 1, (1,0): 8, (1,1): 5, (1,2): 2, (2,0): 9, (2,1):6, (2,2):3}

# for i, l in enumerate(lines):
#     lines[i] = [*l]
    
# for l in lines:
#     prevX = x
#     prevY = y
    
#     for instruct in l:
#         match instruct:
#             case "U":
#                 if ( y + 1) > 2:
#                     continue
#                 y += 1
#             case "D":
#                 if ( y - 1) < 0:
#                     continue
#                 y -= 1
#             case "L":
#                 if ( x - 1) < 0:
#                     continue
#                 x -= 1
#             case "R":
#                 if ( x + 1) > 2:
#                     continue
#                 x += 1
            
    
#     print(numpad[(x,y)], end="")

# print()


#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# x = -2
# y = 0

# numpad = { (0,0): 7, (0,-1):6, (0,-2): 5, (0, 1): 8, (0, 2):9, (1, 0):3, (1,-1): 2, (1, 1): 4, (2, 0): 1, (-1, 0): "B", (-1, -1): "A", (-1, 1): "C", (-2, 0): "D" }

# for i, l in enumerate(lines):
#     lines[i] = [*l]
    
# for l in lines:
#     for instruct in l:
#         prevX = x
#         prevY = y
#         match instruct:
#             case "U":
#                 y += 1
#             case "D":
#                 y -= 1
#             case "L":
#                 x -= 1
#             case "R":
#                 x += 1
                
#         try:
#             numpad[(y, x)]
#         except:
#             x = prevX
#             y = prevY
            
    
#     print(numpad[(y,x)], end="")

# print()