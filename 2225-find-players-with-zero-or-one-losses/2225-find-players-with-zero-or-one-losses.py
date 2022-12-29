class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners ={matches[0][0]:1}
        losers = {matches[0][1]:1}
        size = len(matches)
        for index in range(1,size):
            winners[matches[index][0]] = 1 + winners.get(matches[index][0], 0)
            losers[matches[index][1]] = 1 + losers.get(matches[index][1], 0)
            
        winnerList =[]
        for winner in winners:
            if winner in losers:
                continue
            else:
                winnerList.append(winner)
        loserList = []      
        for loser in losers:
            if losers[loser] > 1:
                continue
            else:
                loserList.append(loser)
                
        return [sorted(winnerList), sorted(loserList)]