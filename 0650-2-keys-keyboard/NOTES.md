def gcd (self, a, b):
if b == 0:
return a
return self.gcd(b, a%b)
def minSteps(self, n: int) -> int:
curr = 1
count = 1
val = 1
flag = True
while val < n:
flag = False
ans = gcd(n,val)
if ans == curr:
val += curr
count += 1
else:
curr = ans
val += curr
count += 2
if flag:
count = 0
return count