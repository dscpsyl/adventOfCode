import sys
import copy

#? Part 1
# with open("data.txt", 'r') as f:
#     line = f.readline().strip()

# line = line.split(",")
# line = [int(l) for l in line]


# # i = opcode, i+1 = input 1, i+2 = input 2, i+3 = destination
# for i in range(0, len(line), 4):
#     match line[i]:
#         case 1:
#             line[line[i+3]] = line[line[i+1]] + line[line[i+2]]
#         case 2:
#             line[line[i+3]] = line[line[i+1]] * line[line[i+2]]
#         case 99:
#             print(line[0])
#             sys.exit()
            
            
#? Part 2
# with open("data.txt", 'r') as f:
#     input = f.readline().strip()

# input = input.split(",")
# MEMORY = [int(l) for l in input]
# OUTPUT = 19690720


# for noun in range(1, 100):
#     for verb in range(1, 100):
#         line = copy.deepcopy(MEMORY)
#         line[1] = noun
#         line[2] = verb
        
#         # i = opcode, i+1 = input 1, i+2 = input 2, i+3 = destination
#         for i in range(0, len(line), 4):
#             match line[i]:
#                 case 1:
#                     line[line[i+3]] = line[line[i+1]] + line[line[i+2]]
#                 case 2:
#                     line[line[i+3]] = line[line[i+1]] * line[line[i+2]]
#                 case 99:
#                     break
#                 case _:
#                     print(f"SOMETHING IS HORRIBLY WRONG")
                    
        
#         if line[0] == OUTPUT:
#             print(100 * noun + verb)
#             sys.exit()
        
        
        