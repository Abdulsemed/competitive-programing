
def gcd(num1,num2):
    if num2 - num1 == 0:
        print (num1)
    else:
        print(1)
 
left, right = map(int, input().split())
gcd(left,right)