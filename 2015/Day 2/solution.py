
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# for index, l in enumerate(lines):
#     lines[index] = l.split('x')


# total = 0

# for box in lines:
#     l = int(box[0])
#     w = int(box[1])
#     h = int(box[2])
    
#     extra = min([l*w, w*h, h*l])
#     surfaceArea = 2*l*w + 2*w*h + 2*h*l
    
#     total += (extra + surfaceArea)
    

# print(total)

#? Part 2
with open("data.txt", 'r') as f:
    lines = [line.strip() for line in f]

for index, l in enumerate(lines):
    lines[index] = l.split('x')


total = 0

for box in lines:
    box = [eval(i) for i in box]
    box.sort()    
    
    part1 = 2 * int(box[0]) + 2 * int(box[1])
    part2 = int(box[0]) * int(box[1]) * int(box[2])
    print(f"Part 1: {part1}, Part 2: {part2}")
    print(f"This box needs{part1+part2}")
    total += (part1 + part2)
    

print(total)