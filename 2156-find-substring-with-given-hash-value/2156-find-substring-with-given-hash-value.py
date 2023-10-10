class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        curr = 0
        left = 0
        right = k-1
        powers = [1] *(k)
        raises= []
        for index in range(1,k):
            powers[index] = powers[index-1] * power
            
        for index in range(k):
            curr += (ord(s[index]) -96) *(powers[index])
            
        for index in range(1,28):
            raises.append(powers[-1] *(index))
            
        while right <= len(s):
            if curr % modulo == hashValue:
                return s[left:right+1]
            else:
                if right +1 >= len(s):
                    break
                curr = ((curr - (ord(s[left]) -96 )) // (power)) +raises[ord(s[right+1] ) -97 ]
                left += 1
                right += 1