import os



#? Part 1
# with open('data.txt', 'r') as f:
#     rucksacks = [line.strip() for line in f]
    
# sum = 0
    
# for index, sack in enumerate(rucksacks):
#     compartment1 = sack[:len(sack)//2]
#     compartment2 = sack[len(sack)//2:]
    
#     for item1 in compartment1:
#         for item2 in compartment2:
#             if item1 == item2:
#                 rightItem = item1
                
#     if not rightItem.isupper():
#         sum += (ord(rightItem) - 96)
#     else:
#         sum += (ord(rightItem) - 38)

# print(sum)


#? Part 2        
# with open('data.txt', 'r') as f:
#     rucksacks = [line.strip() for line in f]
    
# sum = 0

# for starting in range(0, len(rucksacks)-1, 3):
#     for i in rucksacks[starting]:
#         for j in rucksacks[starting+1]:
#             for k in rucksacks[starting+2]:
#                 if i == j == k:
#                     teamLetter = i
    
#     if not teamLetter.isupper():
#         sum += (ord(teamLetter) - 96)
#     else:
#         sum += (ord(teamLetter) - 38)

# print(sum)