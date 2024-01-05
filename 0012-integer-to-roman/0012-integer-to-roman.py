class Solution:
    def intToRoman(self, num: int) -> str:
        dicts = {"I":1,"V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
        count =0
        num = str(num)
        arr = []
        for index in range(len(num)):
            curr = (10**(len(num)-1-index)) * int(num[index])
            while curr >999:
                arr.append("M")
                curr -= 1000
            while curr == 900:
                arr.append("CM")
                curr -= 900
            while curr > 499:
                arr.append("D")
                curr -= 500
            while curr == 400:
                arr.append("CD")
                curr -= 400
            while curr > 99:
                arr.append("C")
                curr -= 100
            while curr == 90:
                arr.append("XC")
                curr -= 90
            while curr > 49:
                arr.append("L")
                curr -= 50
            while curr == 40:
                arr.append("XL")
                curr -= 40
            while curr > 9:
                arr.append("X")
                curr -= 10
            while curr == 9:
                arr.append("IX")
                curr -= 9
            while curr > 4:
                arr.append("V")
                curr -= 5
            while curr == 4:
                arr.append("IV")
                curr -= 4
            while curr > 0:
                arr.append("I")
                curr -= 1
        return "".join(arr)