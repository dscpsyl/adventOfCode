# https://adventofcode.com/2019

from math import floor

#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# total = 0

# values = [eval(l) for l in lines]

# for mass in values:
#     total += floor(mass/3) -2
    
    
# print(total)

#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# total = 0

# def massCalc(mass):
#     global total

#     newMass = floor(mass/3) - 2
#     if newMass <= 0:
#         return
    
#     total += newMass
    
#     massCalc(newMass)


# values = [eval(l) for l in lines]

# for t, mass in enumerate(values):
#     massCalc(mass)
    
    
# print(total)