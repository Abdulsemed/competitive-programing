if __name__ == '__main__':
    N = int(input())
    commands = []
    newList = []
    for index in range(N):
        commands.append(list(input().split(" ")))
    for command in commands:
        size = len(command)
        if size == 2:
            eval("newList."+command[0]+"("+command[1]+")")
        elif size == 3:
            eval("newList."+command[0]+"("+command[1]+","+command[2]+")")
        elif command[0] == "print":
            print(newList)
        else:
            eval("newList."+command[0]+"()")
    
