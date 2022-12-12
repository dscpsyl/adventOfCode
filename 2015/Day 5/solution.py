
#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]
    
# niceStrings = 0

# for l in lines:    
#     vowels = 0
#     bad = False
#     #Check for condition 1
#     # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
#     for i, c in enumerate(l):
#         if i == len(l) - 1:
#             continue
#         if l[i:i+2] in ["ab", "cd", "pq", "xy"]:
#             bad = True
#             break
    
#     if bad:
#         continue
    
#     #Check for condition 2
#     # It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou
#     for c in l:
#         if c in "aeiou":
#             vowels += 1
    
#     if vowels < 3:
#         continue
        
#     #Check for condition 3
#     #  It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     for i, c in enumerate(l):
#         if i == len(l) - 1:
#             continue
#         if l[i] == l[i+1]:
#             niceStrings += 1
#             break
    
    
# print(niceStrings)

#? Part 2
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]
    
# niceStrings = 0

# for l in lines:    
#     bad = False
#     # Condition 1
#     # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     for i, c in enumerate(l):
#         if i == len(l) - 1:
#             bad = True
#         if l[i:i+2] in l[i+2:]:
#             break

#     if bad:
#         continue
    
#     # Condition 2
#     # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
#     for i, c in enumerate(l):
#         if i == len(l) - 2:
#             break
#         if l[i] == l[i+2]:
#             niceStrings += 1
#             break
    
    
# print(niceStrings)