class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = deque(sorted(tokens))
        currScore = 0
        maxim = 0
        while tokens:
            if tokens[0] <= power:
                currScore += 1
                power -= tokens[0]
                tokens.popleft()
            elif currScore > 0:
                currScore -= 1
                power += tokens[-1]
                tokens.pop()
            else:
                break
            maxim = max(maxim, currScore)
                
        return maxim
                
                