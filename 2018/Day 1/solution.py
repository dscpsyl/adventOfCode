# https://adventofcode.com/2018

import sys

#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# freq = 0

# lines = [eval(i) for i in lines]

# for l in lines:
#     freq += l

# print(freq)
    
#? Part 2
with open("data.txt", 'r') as f:
    lines = [line.strip() for line in f]

freq = 0

breaked = False

lines = [eval(i) for i in lines]
 
record = [0]

while True:
    for l in lines:
        print(f"Current freq {freq}, change of {l}, ", end="")
        freq += l
        print(f"new freq {freq}, ", end="")
        
        for q in record:
            if freq == q:
                print("----------------------------------------------------------, ", freq)
                breaked = True
                sys.exit()
        
        if breaked:
            break

        record.append(freq)
        print(f"records has length {len(record)}") 
    
    if breaked:
        break