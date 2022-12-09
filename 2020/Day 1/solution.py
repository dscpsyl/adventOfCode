# https://adventofcode.com/2020

import sys

#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# lines = [eval(i) for i in lines]

# ans = 0

# for l in lines:
#     i = 0
#     while i < len(lines):
#         if l + lines[i] == 2020:
#             ans = l * lines[i]
#             print(ans)
#             sys.exit()
        
#         i+= 1


#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# lines = [eval(i) for i in lines]

# ans = 0

# for l in lines:
#     i = 0
#     while i < len(lines):
#         j = 0
#         while j < len(lines):
#             pot = sum([l, lines[i], lines[j]])
#             if pot == 2020:
#                 ans = l * lines[i] * lines[j]
#                 print(ans)
#                 sys.exit()
#             j+=1
#         i+= 1
        
        
# print(ans)