from copy import deepcopy

#? Part 1
# with open("data.txt", 'r') as f:
#     lines = [line.strip() for line in f]

# gamma = "" # most common 
# epsilon = "" # least common 


# for i in range(len(lines[0])):
#     zeroValue = 0
#     oneValue = 0
#     for j in range(len(lines)):
#         match lines[j][i]:
#             case "0":
#                 zeroValue += 1
#             case "1":
#                 oneValue += 1
#             case _:
#                 print(f"Something has gone wrong")
    
#     if zeroValue > oneValue:
#         gamma += "0"
#         epsilon += "1"
#     else:
#         gamma += "1"
#         epsilon += "0"


# print(int(gamma, 2) * int(epsilon, 2))


#? Part 2
with open("data.txt", 'r') as f:
    lines = [line.strip() for line in f]

oxygenList = deepcopy(lines) # most common
coTwoList = deepcopy(lines) # least common 

oxygen = ""
coTwo = ""


for i in range(len(lines[0])):
    zeroValue = 0
    oneValue = 0
    
    for j in range(len(lines)):
        match lines[j][i]:
            case "0":
                zeroValue += 1
            case "1":
                oneValue += 1
            case _:
                print(f"Something has gone wrong")
    
    if zeroValue > oneValue:
        # oxygen keep all the zeros
        for l in oxygenList:
            if len(oxygenList) == 1:
                oxygen = oxygenList[0]
                break
            
            if l[i] != "0":
                oxygenList.remove(l)
        
        # coTwo keep all the ones
        for l in coTwoList:
            if len(coTwoList) == 1:
                coTwo = coTwoList[0]
                break
            
            if l[i] != "1":
                coTwoList.remove(l)
                
    else:
        # oxygen keep all the one's
        for l in oxygenList:
            if len(oxygenList) == 1:
                oxygen = oxygenList[0]
                break
            
            if l[i] != "1":
                oxygenList.remove(l)
        
        # coTwo keep all the ones
        for l in coTwoList:
            if len(coTwoList) == 1:
                coTwo = coTwoList[0]
                break
            
            if l[i] != "0":
                coTwoList.remove(l)


print(int(oxygen, 2) * int(coTwo, 2))