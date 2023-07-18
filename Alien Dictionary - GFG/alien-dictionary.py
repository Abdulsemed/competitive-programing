#User function Template for python3

from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        ans = []
        sets = set()
        queue = deque()
        dicts = defaultdict(list)
        indegree = {chr(index):0 for index in range(97,97+k)}
        for index in range(1,N):
            val = 0
            size = min(len(alien_dict[index-1]), len(alien_dict[index]))-1
            while alien_dict[index-1][val] == alien_dict[index][val] and val < size:
                val += 1
            if alien_dict[index-1][val] != alien_dict[index][val]:
                dicts[alien_dict[index-1][val]].append(alien_dict[index][val])
                indegree[alien_dict[index][val]] += 1
                sets.add(alien_dict[index-1][val])
                sets.add(alien_dict[index][val])
        
        for key in indegree:
            if key not in sets:
                ans.append(key)
            elif indegree[key] == 0:
                queue.append(key)
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for child in dicts[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return ans
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends