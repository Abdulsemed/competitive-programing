class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        for element in s1:
            s1Dict[element] = 1 + s1Dict.get(element,0)
        s2Dict = {}
        size = len(s2)
        left = 0
        for right in range(size):
            
            if s2[right] in s1Dict:
                if len(s2Dict) == 0:
                    left = right
                if s2Dict.get(s2[right],0) == s1Dict[s2[right]]:
                    while s2Dict[s2[right]] >= s1Dict[s2[right]]:
                        s2Dict[s2[left]] -= 1
                        left += 1 
                s2Dict[s2[right]] = 1 + s2Dict.get(s2[right], 0)
            elif s2[right] not in s1Dict:
                s2Dict = {}
                
            if s2Dict == s1Dict:
                return True
        
        return False