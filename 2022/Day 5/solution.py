import os
from collections import deque


#? Part 1
# with open('data.txt', 'r') as f:
#     lines = [line.strip() for line in f]
    
# stack1 = deque()
# stack2 = deque()
# stack3 = deque()
# stack4 = deque()
# stack5 = deque()
# stack6 = deque()
# stack7 = deque()
# stack8 = deque()
# stack9 = deque()


# stack1.append('N')
# stack1.append('B')
# stack1.append('D')
# stack1.append('T')
# stack1.append('V')
# stack1.append('G')
# stack1.append('Z')
# stack1.append('J')

# stack2.append('S')
# stack2.append('R')
# stack2.append('M')
# stack2.append('D')
# stack2.append('W')
# stack2.append('P')
# stack2.append('F')

# stack3.append('V')
# stack3.append('C')
# stack3.append('R')
# stack3.append('S')
# stack3.append('Z')

# stack4.append('R')
# stack4.append('T')
# stack4.append('J')
# stack4.append('Z')
# stack4.append('P')
# stack4.append('H')
# stack4.append('G')

# stack5.append('T')
# stack5.append('C')
# stack5.append('J')
# stack5.append('N')
# stack5.append('D')
# stack5.append('Z')
# stack5.append('Q')
# stack5.append('F')

# stack6.append('N')
# stack6.append('V')
# stack6.append('P')
# stack6.append('W')
# stack6.append('G')
# stack6.append('S')
# stack6.append('F')
# stack6.append('M')

# stack7.append('G')
# stack7.append('C')
# stack7.append('V')
# stack7.append('B')
# stack7.append('P')
# stack7.append('Q')

# stack8.append('Z')
# stack8.append('B')
# stack8.append('P')
# stack8.append('N')



# stack9.append('W')
# stack9.append('P')
# stack9.append('J')


# stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

# result = lines[0].split('move')
# result1 = result[1].split('from')
# result2 = result1[1].split('to')


# for l in lines:
#     initial = l.split('move')
#     intermediate = initial[1].split('from')
#     parsed = []
#     parsed.append(intermediate[0])
#     parsed.append(intermediate[1].split('to')[0])
#     parsed.append(intermediate[1].split('to')[1])
    
#     for i in range(int(parsed[0])):
#         stacks[int(parsed[2])-1].append(stacks[int(parsed[1])-1].pop())


# for index, stack in enumerate(stacks):
#     print(stack.pop(), end="")
        

#? Part 2
# with open('data.txt', 'r') as f:
#     lines = [line.strip() for line in f]
    
# stack1 = deque()
# stack2 = deque()
# stack3 = deque()
# stack4 = deque()
# stack5 = deque()
# stack6 = deque()
# stack7 = deque()
# stack8 = deque()
# stack9 = deque()


# stack1.append('N')
# stack1.append('B')
# stack1.append('D')
# stack1.append('T')
# stack1.append('V')
# stack1.append('G')
# stack1.append('Z')
# stack1.append('J')

# stack2.append('S')
# stack2.append('R')
# stack2.append('M')
# stack2.append('D')
# stack2.append('W')
# stack2.append('P')
# stack2.append('F')

# stack3.append('V')
# stack3.append('C')
# stack3.append('R')
# stack3.append('S')
# stack3.append('Z')

# stack4.append('R')
# stack4.append('T')
# stack4.append('J')
# stack4.append('Z')
# stack4.append('P')
# stack4.append('H')
# stack4.append('G')

# stack5.append('T')
# stack5.append('C')
# stack5.append('J')
# stack5.append('N')
# stack5.append('D')
# stack5.append('Z')
# stack5.append('Q')
# stack5.append('F')

# stack6.append('N')
# stack6.append('V')
# stack6.append('P')
# stack6.append('W')
# stack6.append('G')
# stack6.append('S')
# stack6.append('F')
# stack6.append('M')

# stack7.append('G')
# stack7.append('C')
# stack7.append('V')
# stack7.append('B')
# stack7.append('P')
# stack7.append('Q')

# stack8.append('Z')
# stack8.append('B')
# stack8.append('P')
# stack8.append('N')



# stack9.append('W')
# stack9.append('P')
# stack9.append('J')


# stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

# result = lines[0].split('move')
# result1 = result[1].split('from')
# result2 = result1[1].split('to')


# for l in lines:
#     initial = l.split('move')
#     intermediate = initial[1].split('from')
#     parsed = []
#     parsed.append(intermediate[0])
#     parsed.append(intermediate[1].split('to')[0])
#     parsed.append(intermediate[1].split('to')[1])
    
#     holding = []
#     for i in range(int(parsed[0])):
#         holding.append(stacks[int(parsed[1])-1].pop())
    
#     for i in range(len(holding)):
#         stacks[int(parsed[2])-1].append(holding.pop())
        


# for index, stack in enumerate(stacks):
#     print(stack.pop(), end="")
    