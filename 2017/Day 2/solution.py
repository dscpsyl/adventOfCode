
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]


# checksum = 0

# for i, l in enumerate(lines):
#     lines[i] = l.split()

# for l in lines:
#     for j in l:
#         j.strip()
    
#     l = [eval(i) for i in l]
#     l.sort()
#     thisSum = int(l[len(l)-1]) - int(l[0])
#     checksum+= thisSum
    
# print(checksum)


#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]


# checksum = 0

# for i, l in enumerate(lines):
#     lines[i] = l.split()

# for l in lines:
#     for j in l:
#         j.strip()
    
#     l = [eval(i) for i in l]
    
#     breaked = False
#     for j in l:
#         i = 0
#         while i < len(l):
#             if (j/l[i]) != 1 and j % l[i] == 0:
#                 checksum += j/l[i]
#                 breaked = True
#             i += 1
    
#         if breaked:
#             break
    
# print(checksum)