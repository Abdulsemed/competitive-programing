def cirno(val):
    andCount = 0
    num = val
    while num & 1 == 0:
        andCount += 1
        num >>= 1
    num = val
    xorCount = 0
    while num ^ 1 == 0:
        xorCount += 1
        num >>= 1
    if xorCount == andCount:
        print(2**xorCount)
    else:
        num = 2**xorCount + (2**andCount)
        holder = num
        curr = 1
        while curr < val:
            if curr^ val and curr & val:
                holder = curr
                break
            curr <<= 1
        print(holder)
 
tests = int(input())
for _ in range(tests):
    num = int(input())
    cirno(num)