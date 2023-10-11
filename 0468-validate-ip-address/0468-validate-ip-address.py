class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        numbers = {"0","1","2","3","4","5","6","7","8","9"}
        alphas = {"A","a","B","b","C","c","D","d","E","e","F","f"}
        
        arr = queryIP.split(".")
        flag = True
        if len(arr) ==4:
            for index in range(4):
                size = len(arr[index])
                if size > 4 or size < 1 or (size > 1 and arr[index][0] == "0"):
                    flag = False
                    break
                for val in range(size): 
                    if arr[index][val] not in numbers:
                        flag = False
                        break
                if flag:
                    intRep = int(arr[index])
                    if intRep > 255 or intRep < 0:
                        flag = False
                        break
                    
            if flag:        
                return "IPv4"
        arr = queryIP.split(":")
        if len(arr) == 8:
            for index in range(8):
                size = len(arr[index])
                if size > 4 or size < 1 :
                    flag = False 
                    break
                for val in range(size):
                    if arr[index][val] not in numbers and arr[index][val] not in alphas:
                        flag = False
                        break
                    
                if not flag: break
            if flag:
                return "IPv6"
            
        return "Neither"