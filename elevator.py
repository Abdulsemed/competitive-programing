def Elevator(walk, elevator,efloor):
    fullwalk = walk * 4
    fullelev = elevator*efloor + elevator*4
    combined = walk * efloor + elevator*(4-efloor)
    print(min(fullelev,fullwalk,combined))

tests = int(input())
for _ in range(tests):
    walk, elevator,efloor = map(int,input().split())
    Elevator(walk, elevator,efloor)
