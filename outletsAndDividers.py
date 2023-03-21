def outlets(student,divSize,divider):
    if student <= 2:
        print(0)
    else:
        minLen = float("inf")
        divider.sort()
        currSum =0
        for index in range(divSize-1,-1,-1):
            currSum += divider[index]
            if currSum+2+index-divSize>= student:
                minLen = min(minLen,divSize-index)
        if minLen == float("inf"):
            minLen = -1              
        print(minLen)
tests = int(input())
for _ in range(tests):
    student, outlet = map(int,input().split())
    dividers = list(map(int,input().split()))
    outlets(student,outlet,dividers)
