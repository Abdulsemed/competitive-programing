def roads(size):
    visited = set()
    count = 0
    for index in range(size):
        rows = list(map(int, input().split()))
        for val in range(size):
            if rows[val] == 1 and (index, val) not in visited:
                count += 1
            visited.add((index,val))
            visited.add((val,index))

    print(count)

size = int(input())
roads(size)