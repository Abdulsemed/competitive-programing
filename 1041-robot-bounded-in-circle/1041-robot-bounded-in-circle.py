class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        lefts = {"N":"E", "E":"S","S":"W", "W":"N"}
        rights = {"N":"W", "W":"S", "S":"E", "E":"N"}
        go = {"N":(0,1), "E":(1,0), "W":(-1,0), "S":(0,-1)}
        curr = "N"
        path = [0,0]
        for inst in instructions:
            if inst == "L":
                curr = lefts[curr]
            elif inst == "R":
                curr = rights[curr]
            else:
                path[0]+= go[curr][0]
                path[1]+= go[curr][1]
            
        if path == [0,0] or curr != "N":
                return True
        return False
                