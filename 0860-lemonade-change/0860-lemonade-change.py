class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twentys = 0
        remains = 0
        for element in bills:
            if element == 5:
                fives += 1
            elif element == 10:
                if fives > 0:
                    fives -= 1
                else:
                    return False
                tens += 1
            else:
                if fives >0 and tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                twentys += 1
        return True
                
                