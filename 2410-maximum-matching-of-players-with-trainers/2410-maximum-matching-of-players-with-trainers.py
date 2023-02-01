class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        playerPointer = 0
        playerSize = len(players)
        trainerSize = len(trainers)
        trainerPointer = 0
        matches = 0
        while playerPointer < playerSize and trainerPointer < trainerSize:
            if players[playerPointer] <= trainers[trainerPointer]:
                matches += 1
                playerPointer += 1
                trainerPointer += 1
            else:
                trainerPointer += 1
        return matches