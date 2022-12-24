class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"  
        decrypted = ""
        temporaryHolder = ""
        stack = []
        for elements in s:
            if elements !="#":
                stack.append(elements)
            else:
                index = stack.pop() + stack.pop()
                index = index[::-1]
                temporaryHolder += alphabets[int(index)-1]
                temporaryHolder = self.decrypter(stack, temporaryHolder,alphabets)
                decrypted += temporaryHolder[::-1]
                stack = []
                temporaryHolder = ""
                
        if stack:
            temporaryHolder = self.decrypter(stack, temporaryHolder,alphabets)
            decrypted += temporaryHolder[::-1]
        return decrypted
                
    def decrypter (self, stack, decrypted,alphabets):        
        while stack:
            decrypted += alphabets[int(stack[-1])-1]
            stack.pop()
        return decrypted
        
        