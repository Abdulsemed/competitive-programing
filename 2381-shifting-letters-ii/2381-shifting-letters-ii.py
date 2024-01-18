class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefixes = [0]*(len(s)+1)
        for src, end, direction in shifts:
            if direction:
                prefixes[src] += 1
                prefixes[end+1] -= 1
            else:
                prefixes[src] -= 1
                prefixes[end+1] += 1
                
        for index in range(1,len(s)+1):
            prefixes[index] += prefixes[index-1]
        arr = []
        for index in range(len(s)):
            val = (((ord(s[index]) + prefixes[index])-97)%26) + 97
            arr.append(chr(val))
        return ''.join(arr)