def tshirt(size1, size2):
    if size1[-1] == size2[-1]:
        if len(size1) > len(size2):
            if size1[-1] == "S":
                print("<")
            else:
                print(">")
        elif len(size1) == len(size2):
            print("=")
        else:
            if size1[-1] == "S":
                print(">")
            else:
                print("<")
    elif size1[-1] > size2[-1]:
        print("<")
    else:
        print(">")
        
    
    
size = int(input())
for _ in range(size):
    size1, size2 = input().split(" ")
    tshirt(size1, size2)
