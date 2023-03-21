def karen(recipe,admiss,questions):
    arr=[0]*(200002)
    for _ in range(recipe):
        rec1 = list(map(int,input().split()))
        arr[rec1[0]] += 1
        arr[rec1[1]+1] -= 1
    for index in range(1,200002):
        arr[index] += arr[index-1]
    for index in range(1,200002):
        if arr[index] >= admiss:
            arr[index] = 1
        else:
            arr[index] = 0
        arr[index] += arr[index-1] 
    for _ in range(questions):
        quest = list(map(int,input().split()))
        print(arr[quest[1]]-arr[quest[0]-1])
 
numRec, admiss,question = map(int,input().split())
karen(numRec,admiss,question)
