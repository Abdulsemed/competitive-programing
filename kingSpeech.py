def stuter(word):
    stut = word[0]+word[1] +"... " + word+"?"
    print(stut)
    
  
 
size = int(input())
for _ in range(size):
    word = input()
    stuter(word)
