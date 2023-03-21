import math

def emotes(arr,size,m,k):
    arr.sort()
    currSum = m//(k+1) * k *arr[-1] + int(m/(k+1))* arr[-2] + m%(k+1) * arr[-1]
    print(currSum)
size,m,k = map(int,input().split(" "))
arr = list(map(int,input().split()))
emotes(arr,size,m,k)
