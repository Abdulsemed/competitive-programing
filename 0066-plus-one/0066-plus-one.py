class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = str(digits[-1] + 1)
        if len(val) == 1:
            digits[-1] = int(val)
        else:
            size = len(digits)
            for index in range(size-1,-1,-1):
                if digits[index] + 1 > 9:
                    if index == 0:
                        digits[index] = 1
                        digits.append(0)
                    else:
                        digits[index] = 0 
                    continue
                else:
                    digits[index] += 1
                break
        return digits