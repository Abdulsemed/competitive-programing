def func(n,m,arr,a,b):
    happy = 0
    for num in arr:
        if num in a:
            happy += 1
        if num in b:
            happy -= 1
    print(happy)
    
n = input().split(" ")
arr1 =input().split(" ")   
a = set(input().split(" "))
b = set(input().split(" ") )
func(int(n[0]),int(n[1]),arr1,a,b)
