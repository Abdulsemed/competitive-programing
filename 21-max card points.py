def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        beg = 0
        end = len(cardPoints)-1
        max_score = 0
        if len(cardPoints) == k:
            return sum(cardPoints)
        beg_index = k-1
        end_index = len(cardPoints)-k
        score_end = sum(cardPoints[len(cardPoints)-k:len(cardPoints)])
        score_beg = sum(cardPoints[:k])
        for index in range(k):
            if score_beg > score_end:
                max_score += cardPoints[beg]
                score_beg -= cardPoints[beg]
                score_end -= cardPoints[end_index]
                end_index += 1
                beg += 1
            elif score_end > score_beg:
                max_score += cardPoints[end]
                score_beg -= cardPoints[beg_index]
                score_end -= cardPoints[end]
                beg_index -= 1
                end -= 1
            else:
                max_score += cardPoints[end]
                score_beg -= cardPoints[beg_index]
                score_end -= cardPoints[end]
                beg_index -= 1
                end -= 1
        return max_score
