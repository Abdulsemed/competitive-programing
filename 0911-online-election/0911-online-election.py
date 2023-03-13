class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.sizeTime = len(times)
        self.dicts = {}
        self.answers = []
        for index in range(self.sizeTime):
            self.dicts[self.persons[index]] = 1 + self.dicts.get(self.persons[index],0)
            if self.answers:
                if self.dicts[self.persons[index]] >= self.dicts[self.answers[-1]]:
                    self.answers.append(self.persons[index])
                else:
                    self.answers.append(self.answers[-1])
            else:
                self.answers.append(self.persons[index])
    def q(self, t: int) -> int:
        left = 0
        right = self.sizeTime-1
        while left<=right:
            mid = left + (right-left)//2
            if self.times[mid] == t:
                right = mid
                break
            elif self.times[mid] < t:
                left = mid +1
            else:
                right = mid - 1
        return self.answers[right]
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)