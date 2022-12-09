import os

#? Part 1
# opponentHand = {"A" : "Rock", "B" : "Paper", "C" : "Scissors"}
# myHand = {"X" : "Rock", "Y" : "Paper", "Z" : "Scissors"}
# handScores = {"Rock" : 1, "Paper" : 2, "Scissors" : 3}

# # Read the predictions
# predictions = []
# with open('data.txt', 'r') as file:
#     predictions = [line.strip() for line in file]

# # Translate the predictions into hands
# decryptedPredictions = []
# for index, value in enumerate(predictions):
#     roundHands = value.split(" ")
#     roundHands[0] = opponentHand[roundHands[0]]
#     roundHands[1] = myHand[roundHands[1]]
#     decryptedText = ",".join(roundHands)
#     decryptedPredictions.append(decryptedText)
    
# # print(decryptedPredictions)
    
# # Find value of each round and sum it all up
# sum = 0
#     # 0 if you lost, 3 if the round was a draw, and 6 if you won
# for index, value in enumerate(decryptedPredictions):
#     # Split hands
#     hands = value.split(',')
#     # Add value of hand
#     sum += handScores[hands[1]]
#     #Check for loss cases
#     if hands[0] == "Rock" and hands[1] == "Scissors" or hands[0] == "Scissors" and hands[1] == "Paper" or hands[0] == "Paper" and hands[1] == "Rock":
#         continue
#     # Check to see if draw or win to add values
#     if hands[0] == hands[1]:
#         sum += 3
#     else:
#         sum += 6
        
# print(sum)

#? Part 2
# opponentHand = {"A" : "Rock", "B" : "Paper", "C" : "Scissors"}
# roundCondition = {"X" : "Loose", "Y" : "Draw", "Z" : "Win"}

# loosingHand = {"Rock" : "Scissors", "Scissors" : "Paper", "Paper" : "Rock"}
# winningHand = {"Scissors" : "Rock", "Paper" : "Scissors", "Rock" : "Paper"}

# handScores = {"Rock" : 1, "Paper" : 2, "Scissors" : 3}

# # Read the predictions
# predictions = []
# with open('data.txt', 'r') as file:
#     predictions = [line.strip() for line in file]
    
# # Translate predictions into opponent hand and round condition
# decryptedPredictions = []
# for index, value in enumerate(predictions):
#     roundHands = value.split(" ")
#     roundHands[0] = opponentHand[roundHands[0]]
#     roundHands[1] = roundCondition[roundHands[1]]
#     decryptedText = ",".join(roundHands)
#     decryptedPredictions.append(decryptedText)
    
# # Find value of each round and sum it up
# sum = 0
# for index, value in enumerate(decryptedPredictions):
#     roundHands = value.split(",")
#     # Easiest one, check if it's a draw
#     if roundHands[1] == "Draw":
#         sum += 3
#         sum += handScores[roundHands[0]]
#     # Now see if it is a loss
#     elif roundHands[1] == "Loose":
#         sum += handScores[loosingHand[roundHands[0]]]
#     # Now we know it has to be a wining condition
#     else:
#         sum += 6
#         sum += handScores[winningHand[roundHands[0]]]

# print(sum)
        
    
    