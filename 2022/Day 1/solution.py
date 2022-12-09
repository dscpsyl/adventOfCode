import os

#? Part 1
# with open('data.txt', 'r') as file:
#     listOfLines = file.readlines()


# greatestCalories = 0
# totalCurrentCalories = 0
# for l in listOfLines:
#     if l != '\n':
#         totalCurrentCalories += int(l)
#     else:
#         if totalCurrentCalories > greatestCalories:
#             greatestCalories = totalCurrentCalories
#         totalCurrentCalories = 0

# print(greatestCalories)

#? Part 2
# with open('data.txt', 'r') as file:
#     listOfLines = file.readlines()


# allCalories = []
# totalCurrentCalories = 0
# topThreeCalories = 0
# for l in listOfLines:
#     if l != '\n':
#         totalCurrentCalories += int(l)
#     else:
#         allCalories.append(totalCurrentCalories)
#         totalCurrentCalories = 0

# allCalories.sort(reverse=True)

# for i in range (3):
#     topThreeCalories += allCalories[i]

# print(topThreeCalories)