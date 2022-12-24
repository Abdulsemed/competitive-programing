class Solution:
    def interpret(self, command: str) -> str:
        parser = {"()":"o","(al)":"al"}
        stack = ""
        interprated = ""
        for elements in command:
            if  elements == "G":
                interprated += elements
            elif elements != ")":
                stack +=elements
                
            else:
                stack += ")" 
                interprated += parser[stack]
                stack=""
        return interprated
                