class Tier:
def __init__(self):
self.children = [[None,0] for index in range(26)]
self.is_end = False
def insert(self,word,prev):
curr =self
possible = []
index = 0
for letter in word:
asci = ord(letter) - 97
if curr.children[asci][0] == None:
curr.children[asci] = [Tier(), 0]
curr.children[asci][1] += 1
if index < len(prev) and prev[index]  == letter and curr.children[asci][1] > 1:
possible.append(letter)
curr = curr.children[asci][0]
index += 1
curr.is_end = True
return ''.join(possible)
class Solution:
def longestWord(self, words: List[str]) -> str:
obj = Tier()
words.sort()
ans = ""
prev = words[0]
obj.insert(words[0],"")
for index in range(1,len(words)):
possible = obj.insert(words[index],words[index-1])
print(words[index],",",possible,"," ,ans)
if possible == words[index-1]:
ans = words[index]
elif possible < ans:
ans = possible
if not ans and len(prev) == 1:
ans = prev
return ans