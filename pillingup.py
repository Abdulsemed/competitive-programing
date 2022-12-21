def func(arr, size):
    beg = 0 
    end = size-1
    if int(arr[end])> int(arr[beg]):
        top = int(arr[end])
        end -= 1
    else:
        top = int(arr[beg])
        beg += 1
    while beg <= end:
        if int(arr[end]) <= int(arr[beg]) and top>= int(arr[beg]):
            top = int(arr[beg])
            beg += 1   
        elif int(arr[end]) > int(arr[beg]) and top >= int(arr[end]):
            top = int(arr[end])
            end -= 1 
        else:
            return "No"
    return "Yes"
        
    
    

t = int(input())
for i in range(t):
    size = int(input())
    arr = input().split(" ")
    print(func(arr, size))
