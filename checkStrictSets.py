def superSet(aSet, nSets):
    flag = True
    for elements in nSets:
        if not aSet.issuperset(elements):
            flag = False
            break
        elif aSet == elements:
            flag = False
            break
    print(flag)
    
aSet = set(input().split(" "))
nSize = int(input())
nSets = []
for index in range(nSize):
    nSets.append(set(input().split(" ")))

superSet(aSet,nSets)
