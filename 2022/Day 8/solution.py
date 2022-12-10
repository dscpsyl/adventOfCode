
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# for index, line in enumerate(lines):
#     lines[index] = [*line]

# edgeTrees = (2*len(lines[0])) + (2*(len(lines)-2))
# innerTrees = 0

# for i in range(1, len(lines)-1):
#     for j in range(1, len(lines[i])-1):
#         curr = lines[i][j]
        
#         # check up (constant j)
#         k = i-1
#         while k >= 0:
#             if not curr > lines[k][j]:
#                 break
#             k -= 1
#         else:
#             innerTrees += 1
#             continue
        
#         # check down (constant j)
#         k = i+1
#         while k < len(lines):
#             if not curr > lines[k][j]:
#                 break
#             k += 1
#         else:
#             innerTrees += 1
#             continue
    
#         # check left (constant i)
#         l = j-1
#         while l >= 0:
#             if not curr > lines[i][l]:
#                 break
#             l -= 1
#         else:
#             innerTrees += 1
#             continue
    
#         # check right  (constant i)
#         l = j+1
#         while l < len(lines):
#             if not curr > lines[i][l]:
#                 break
#             l += 1
#         else:
#             innerTrees += 1
#             continue

# answer = innerTrees + edgeTrees
# print(answer)

#? Part 2
with open("data.txt", 'r') as f:
    lines = [line.strip() for line in f]

for index, line in enumerate(lines):
    lines[index] = [*line]

highestScore = 0

for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-1):
        curr = lines[i][j]
        up = 1
        down = 1
        left = 1
        right = 1
        
        # check up (constant j)
        k = i-1
        while k >= 0:
            if curr > lines[k][j]:
                up += 1
            else:
                break
            k -= 1
        else:
            up -= 1
        
        # check down (constant j)
        k = i+1
        while k < len(lines):
            if curr > lines[k][j]:
                down += 1
            else:
                break
            k += 1
        else:
            down -= 1
    
        # check left (constant i)
        l = j-1
        while l >= 0:
            if curr > lines[i][l]:
                left += 1
            else:
                break
            l -= 1
        else:
            left -= 1
    
        # check right  (constant i)
        l = j+1
        while l < len(lines):
            if curr > lines[i][l]:
                right += 1
            else:
                break
            l += 1
        else:
            right -= 1
        
        # compare viewing score
        score = up * down * left * right
        if score > highestScore:
            highestScore = score
            print(f"Checking {i+1}, {j+1}, value {curr} | Up score {up} | Down score {down} | left score {left} | right score {right} | Final score {score}", end = "\n")

print(highestScore)