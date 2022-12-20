def func(n, words):
    a={}
    for w in words:
        a[w] = 1 + a.get(w,0)
    print(len(a))
    for wor in a.values():
        print(wor, end=" ")     
    
size = int(input())
word = []
for i in range(size):
    word.append(input())
func(size,word)
