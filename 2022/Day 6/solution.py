import os
import sys

#? Part 1
# with open('data.txt') as f:
#     lines = [line.strip() for line in f]


# stream = lines[0]


# headderStream = [stream[0], stream[1], stream[2], stream[3]]
# stream = stream[4:]
# bufferChecked = 4

# def checkBuffer(s):
#     return len(set(s)) == len(s)
            


# for c in stream:
#     if checkBuffer(headderStream):
#         print(bufferChecked)
#         sys.exit()
#     else:
#         headderStream.pop(0)
#         headderStream.append(stream[0])
#         stream = stream[1:]
#         bufferChecked += 1


#? Part 2
# with open('data.txt') as f:
#     lines = [line.strip() for line in f]


# stream = lines[0]

# headderStream = []

# for i in range(14):
#     headderStream += stream[i]

# stream = stream[14:]
# bufferChecked = 14

# def checkBuffer(s):
#     return len(set(s)) == len(s)
            


# for c in stream:
#     if checkBuffer(headderStream):
#         print(bufferChecked)
#         sys.exit()
#     else:
#         headderStream.pop(0)
#         headderStream.append(stream[0])
#         stream = stream[1:]
#         bufferChecked += 1