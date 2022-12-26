def difference (englishNews, englishRoll, frenchNews, frenchRoll):
    countDiffrence = len(englishRoll.difference(frenchRoll))
    print(countDifference)
    
englishNews = int(input())
englishRoll = set(input().split(" "))
frenchNews = int(input()) 
frenchRoll = set(input().split(" "))  

difference(englishNews, englishRoll, frenchNews, frenchRoll)
