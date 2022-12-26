def union (englishNews, englishRoll, frenchNews, frenchRoll):
    countUnion = len(englishRoll.union(frenchRoll))
    print(countUnion)
    
englishNews = int(input())
englishRoll = set(input().split(" "))
frenchNews = int(input()) 
frenchRoll = set(input().split(" "))  

union(englishNews, englishRoll, frenchNews, frenchRoll)
