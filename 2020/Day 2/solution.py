
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# parts = [l.split(":") for l in lines]

# valids = 0

# for i, p in enumerate(parts):
#     policy = p[0].split()
#     bounds = policy[0].split("-")
#     password = p[1].strip()
    
#     parts[i] = [bounds[0], bounds[1], policy[1], password]

# for p in parts:
#     n = p[3].count(p[2])
#     if n >= int(p[0]) and n <= int(p[1]):
#         valids += 1

# print(valids)

#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# parts = [l.split(":") for l in lines]

# valids = 0

# for i, p in enumerate(parts):
#     policy = p[0].split()
#     bounds = policy[0].split("-")
#     password = p[1].strip()
    
#     parts[i] = [bounds[0], bounds[1], policy[1], password]

# for p in parts:
#     c1 = p[3][int(p[0])-1]
#     c2 = p[3][int(p[1])-1]
    
#     if bool(c1 == p[2]) != bool(c2 == p[2]):
#         valids +=1

# print(valids)