class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num))-2
        val = ["0","b"]
        val.extend(["1"]*length)
        val = int(''.join(val),2)
        return val^num