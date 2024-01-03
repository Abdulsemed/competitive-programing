class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        idx = 0
        curr = 0
        while idx < len(bank) and curr == 0:
            curr = bank[idx].count("1")
            idx += 1
        for index in range(idx, len(bank)):
            curr2 = bank[index].count("1")
            if curr2 == 0:
                continue
            count += (curr2*curr)
            curr = curr2
            
        return count