# https://adventofcode.com/2016

import sys

#? part 1
# with open("data.txt", 'r') as f:
#     instructions = f.readline()

# l = instructions.split(", ")

# for i, e in enumerate(l):
#     l[i] = [e[0],e[1:]]

# xBlocks = 0
# yBlocks = 0

# # (0 = N, 90 = E, 180 = S, 270 = W)
# pov = 0

# def updatePOV(lastPOV, face):
#     newPOV = lastPOV
    
#     if face == 'R':
#         newPOV += 90
#     elif face == 'L':
#         newPOV -= 90    
#     else:
#         print(f"HELP ME IDK WHERE I'M FACING")
    
#     if newPOV >= 360:
#         newPOV -= 360
    
#     if newPOV < 0:
#         newPOV += 360
    
#     return newPOV

# for step in l:
#     pov = updatePOV(pov, step[0])
    
#     if pov == 0:
#         yBlocks += int(step[1])
#     elif pov == 90:
#         xBlocks += int(step[1])
#     elif pov == 180:
#         yBlocks -= int(step[1])
#     elif pov == 270:
#         xBlocks -= int(step[1])
    
    
# print(abs(xBlocks) + abs(yBlocks))


#? Part 2
# with open("data.txt", 'r') as f:
#     instructions = f.readline()

# l = instructions.split(", ")

# for i, e in enumerate(l):
#     l[i] = [e[0],e[1:]]

# xBlocks = 0
# yBlocks = 0

# # (0 = N, 90 = E, 180 = S, 270 = W)
# pov = 0
# visitedBlocks = [(0,0)]
# lastCord = (0,0)

# def updatePOV(lastPOV, face):
#     newPOV = lastPOV
    
#     if face == 'R':
#         newPOV += 90
#     elif face == 'L':
#         newPOV -= 90    
#     else:
#         print(f"HELP ME IDK WHERE I'M FACING")
    
#     if newPOV >= 360:
#         newPOV -= 360
    
#     if newPOV < 0:
#         newPOV += 360
    
#     return newPOV

# for step in l:
#     # record last block
#     lastCord = (xBlocks, yBlocks)
    
#     #update pov
#     pov = updatePOV(pov, step[0])
    
#     #update count
#     if pov == 0:
#         yBlocks += int(step[1])
#     elif pov == 90:
#         xBlocks += int(step[1])
#     elif pov == 180:
#         yBlocks -= int(step[1])
#     elif pov == 270:
#         xBlocks -= int(step[1])
    
#     # store current 
#     visitedBlocks.append((xBlocks, yBlocks))
    
    
#     # add all blocks between new and last step
#     if pov == 0:
#         # lastCord y < current y
#         for i in range(lastCord[1]+1, yBlocks):
#             visitedBlocks.append((xBlocks, i))
#     elif pov == 90:
#         # lasCord x < current x
#         for i in range(lastCord[0]+1, xBlocks):
#             visitedBlocks.append((i, yBlocks))
#     elif pov == 180:
#         # lastCord y > current y
#         for i in range(yBlocks+1, lastCord[1]):
#             visitedBlocks.append((xBlocks, i))
#     elif pov == 270:
#         # lasCord x > current x
#         for i in range(xBlocks+1, lastCord[0]):
#             visitedBlocks.append((i, yBlocks))
    
    
#     print(step, pov, visitedBlocks)
    
#     # check if visited
#     for i, visited in enumerate(visitedBlocks):
#         for j in range(len(visitedBlocks)):
#             if visitedBlocks[j] == visited and j != i:
#                 print(abs(visited[0]) + abs(visited[1]))
#                 sys.exit()