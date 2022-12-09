import os
from anytree import Node, RenderTree, Resolver, PostOrderIter #https://anytree.readthedocs.io/en/latest/index.html

#? Part 1
# MAXSIZE = 100000
# answer = 0

# with open('data.txt', 'r') as f:
#     lines = [line.strip() for line in f]


# fileSystem = Node(name="root", parent=None, dir=True, size=0)


# lsActive = False
# dirInFolder = []
# r = Resolver('name')
# currentParentNode = None

# def cdCommand(command):
#     global lsActive, currentParentNode, dirInFolder
#     arg = command[5:]
    
#     if arg == '/':
#         currentParentNode = fileSystem
#         return
        
#     if lsActive:
#         for d in dirInFolder:
#             Node(name=d, parent=currentParentNode, dir=True, size=0)
#         dirInFolder = []
#         lsActive = False
        
#     if arg == "..":
#         currentParentNode = currentParentNode.parent
#         return
    
#     currentParentNode = r.get(currentParentNode, arg)
    
#     return
        
# def parseFile(command):
#     args = command.split(" ")
#     Node(name=args[1], size=int(args[0]), parent=currentParentNode, dir=False)
#     return 

# def dirList(command):
#     global dirInFolder
    
#     arg = command[4:]
    
#     dirInFolder.append(arg)
    
#     return
    

# for command in lines:
#     match command[:3]:
#         case "$ c":
#             cdCommand(command)
#         case "$ l":
#             lsActive = True
#         case "dir":
#             dirList(command)
#         case _:
#             parseFile(command)
            

# for node in PostOrderIter(fileSystem):
#     if not node.dir: # node is a file
#         continue
#     elif node.is_leaf: #node is leaf directory
#         node.size = 0
#     else:
#         node.size = sum([child.size for child in node.children])
    

# for node in PostOrderIter(fileSystem):
#     if not node.dir:
#         continue
    
#     if node.size > MAXSIZE:
#         continue
    
#     answer += node.size
    

# print(answer)



#? Part 2
# TOTALDISKSIZE = 70000000
# MAXSIZE = 100000
# REQUIREDSPACE = 30000000
# answer = 0

# with open('data.txt', 'r') as f:
#     lines = [line.strip() for line in f]


# fileSystem = Node(name="root", parent=None, dir=True, size=0)


# lsActive = False
# dirInFolder = []
# r = Resolver('name')
# currentParentNode = None

# def cdCommand(command):
#     global lsActive, currentParentNode, dirInFolder
#     arg = command[5:]
    
#     if arg == '/':
#         currentParentNode = fileSystem
#         return
        
#     if lsActive:
#         for d in dirInFolder:
#             Node(name=d, parent=currentParentNode, dir=True, size=0)
#         dirInFolder = []
#         lsActive = False
        
#     if arg == "..":
#         currentParentNode = currentParentNode.parent
#         return
    
#     currentParentNode = r.get(currentParentNode, arg)
    
#     return
        
# def parseFile(command):
#     args = command.split(" ")
#     Node(name=args[1], size=int(args[0]), parent=currentParentNode, dir=False)
#     return 

# def dirList(command):
#     global dirInFolder
    
#     arg = command[4:]
    
#     dirInFolder.append(arg)
    
#     return
    

# for command in lines:
#     match command[:3]:
#         case "$ c":
#             cdCommand(command)
#         case "$ l":
#             lsActive = True
#         case "dir":
#             dirList(command)
#         case _:
#             parseFile(command)
            

# for node in PostOrderIter(fileSystem):
#     if not node.dir: # node is a file
#         continue
#     elif node.is_leaf: #node is leaf directory
#         node.size = 0
#     else:
#         node.size = sum([child.size for child in node.children])
    

# avalSpace = TOTALDISKSIZE - fileSystem.size
# neededSpace = REQUIREDSPACE - avalSpace

# smallestDelta = neededSpace

# for node in PostOrderIter(fileSystem):
#     if not node.dir:
#         continue
#     if node.size < neededSpace:
#         continue
    
#     currentDelta = node.size - neededSpace
    
#     if currentDelta < smallestDelta:
#         smallestDelta = currentDelta
#         answer = node.size
    
    
# print(answer)
    