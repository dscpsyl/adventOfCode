with open("data.txt", 'r') as f:
    lines = [line.strip() for line in f]

for index, line in enumerate(lines):
    lines[index] = [*line]

edgeTrees = (2*len(lines[0])) + (2*(len(lines)-2))
innerTrees = 0



    

answer = innerTrees + edgeTrees
print(answer)