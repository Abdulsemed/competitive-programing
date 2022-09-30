def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_parenthesis = []
        flag = True
        for elt in s:
            if elt == "(" or elt == "{" or elt == "[":
                stack_parenthesis.append(elt)
            elif (elt == ")" or elt == "}" or elt == "]") and len(stack_parenthesis) > 0:
                if elt == ")" and stack_parenthesis[len(stack_parenthesis)-1] == "(":
                    stack_parenthesis.pop()
                elif elt == "}" and stack_parenthesis[len(stack_parenthesis)-1] == "{":
                    stack_parenthesis.pop()
                elif elt == "]" and stack_parenthesis[len(stack_parenthesis)-1] == "[":
                    stack_parenthesis.pop()
                else:
                    flag = False
                    break
            else:
                flag = False
                break

        if(len(stack_parenthesis)!= 0):
            flag = False
        return flag
