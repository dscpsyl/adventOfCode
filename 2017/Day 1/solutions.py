# https://adventofcode.com/2017

#? Part 1
# with open("data.txt", 'r') as f:
#     lines = f.readline()
    

# string = [*lines]
# string =[eval(i) for i in string]

# total = 0

# for i, l in string:
#     if i == len(string-1):
#         if l == string[0]:
#             total += l
#             continue
#         else:
#             continue
    
#     if l == string[i+1]:
#         total += l
        
# print(total)


#? Part 2
# with open("data.txt", 'r') as f:
#     lines = f.readline()
    

# string = [*lines]
# string =[eval(i) for i in string]

# total = 0

# for i, l in enumerate(string):
#     halfIndex = i + len(string)/2
#     if halfIndex >= len(string):
#         halfIndex = halfIndex - len(string)
        
#     if l == string[int(halfIndex)]:
#         total += l
        
# print(total)