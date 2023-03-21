def immigration(names,size,queries,query):
    index = 0
    val = 0
    while val < query and index < size:
        if names[index] > queries[val] :
            print(index)
            val+= 1
            index = 0
        elif index == size -1:
            print(index+1)
            index = 0
            val += 1
        else:
            index += 1

size = int(input())
names = list(input().split())
query = int(input())
queries = []
for _ in range(query):
    queries.append(input())
immigration(names,size,queries,query)
