import os


#? Part 1
# with open('data.txt', 'r') as f:
#     lines = [line.strip() for line in f]
    
# total = 0

# for l in lines:
#     pair = l.split(",")
    
#     if int(pair[0][:pair[0].index('-')]) == int(pair[1][:pair[1].index('-')]):
#         total += 1
#         continue
    
#     if int(pair[0][:pair[0].index('-')]) > int(pair[1][:pair[1].index('-')]):
#         pair[0], pair[1] = pair[1], pair[0]
    
#     if int(pair[0][pair[0].index('-')+1:len(pair[0])]) >= int(pair[1][pair[1].index('-')+1:len(pair[1])]):
#         total += 1

# print(total)


#? Part 2
# with open('data.txt', 'r') as f:
#     lines = [line.strip() for line in f]
    
# total = 0

# for l in lines:
#     pair = l.split(",")
    
#     if int(pair[0][:pair[0].index('-')]) == int(pair[1][:pair[1].index('-')]):
#         total += 1
#         continue

#     if int(pair[0][:pair[0].index('-')]) > int(pair[1][:pair[1].index('-')]):
#         pair[0], pair[1] = pair[1], pair[0]

#     if int(pair[0][pair[0].index('-')+1:len(pair[0])]) >= int(pair[1][:pair[1].index('-')]):
#         total += 1

# print(total)

