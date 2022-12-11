
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line for line in f]

# lines = [l.split() for l in lines]

# for i, l in enumerate(lines):
#     sides = [side.strip() for side in l]
#     lines[i] = [int(side) for side in sides]

# validTriangles = 0

# for l in lines:
#     if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
#         validTriangles += 1

# print(validTriangles)

#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line for line in f]

# lines = [l.split() for l in lines]

# for i, l in enumerate(lines):
#     sides = [side.strip() for side in l]
#     lines[i] = [int(side) for side in sides]

# validTriangles = 0

# for i in range(0, len(lines), 3):
#     for j in range(3):
#         if lines[i][j] + lines[i+1][j] > lines[i+2][j] and lines[i+1][j] + lines[i+2][j] > lines[i][j] and lines[i][j] + lines[i+2][j] > lines[i+1][j]:
#             validTriangles += 1

# print(validTriangles)