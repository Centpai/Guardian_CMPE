playerA = ['onic', 'jungle',"kairi", "carry"]
playerB = ["onic", "mid", "sanz","monster"]
playerC= ["onic", "bot","kelra","prodigy"]

playerGroup_list = list(zip(playerA, playerB, playerC))
print(playerGroup_list)
print(playerGroup_list[2])
print(playerGroup_list[2][1])

playerGroup_list = playerA + playerB + playerC
print(playerGroup_list)

playerA.extend(playerB)
playerA.extend(playerC)
print(playerA)


playerA = ['onic', 'jungle',"kairi", "carry"]
playerB = ["onic", "mid", "sanz","monster"]
playerGroupListOfSet =[playerA, playerB,]
print(playerGroupListOfSet)

