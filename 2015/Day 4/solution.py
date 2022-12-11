from hashlib import md5
from sys import exit


#? Part 1
# with open("data.txt", 'r') as f:
#     line = f.readline().strip()
    
# i = 0
# while True:
#     test = line + str(i)
#     result = md5(test.encode()).hexdigest()
    
#     if result[:5] == "00000":
#         print(i)
#         exit()
        
#     i += 1


#? Part 2
# with open("data.txt", 'r') as f:
#     line = f.readline().strip()
    
# i = 0
# while True:
#     test = line + str(i)
#     result = md5(test.encode()).hexdigest()
    
#     if result[:6] == "000000":
#         print(i)
#         exit()
        
#     i += 1