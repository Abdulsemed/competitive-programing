def order(sizeA, sizeB, sizeAb):
    count = 2*sizeAb
    if sizeA >= sizeB:
        val = 2*(sizeB)
        count += val
        sizeA -= sizeB
        sizeB = 0
    else:
        val = 2*(sizeA)
        count += val+1
        sizeA = 0
        sizeB -= (sizeA+1)
    if sizeA >0:
        count += 1
    print(count)
 
inputs = list(map(int, input().split(" ")))
order(inputs[0], inputs[1], inputs[2])
