def composition(prog,maths):
    print(min(prog,maths,(prog+maths)//4))

tests = int(input())
for _ in range(tests):
    prog, maths = map(int,input().split())
    composition(prog,maths)
