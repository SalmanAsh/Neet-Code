#
# Complete the 'equalTeamSkill' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY teamA
#  2. INTEGER_ARRAY teamB
#

def equalTeamSkill(teamA, teamB):
    # Write your code here
    sumA = sum(teamA)
    sumB = sum(teamB)
    
    zeroA = 0
    for i in range(len(teamA)):
        if teamA[i] == 0:
            zeroA += 1
            
    zeroB = 0
    for i in range(len(teamB)):
        if teamB[i] == 0:
            zeroB += 1
    
    possSum = max(sumA + zeroA, sumB + zeroB)