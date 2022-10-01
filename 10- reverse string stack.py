def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for elt in s:
            if elt == "(" or elt.isalpha():
                stack.append(elt)
            else:
                holder = []
                index = len(stack)-1
                while index >= 0:
                    if stack[index] == "(":
                        break
                    holder.append(stack[index])
                    index -= 1
                stack = stack[:index]
                stack.extend(holder)
        return ''.join(stack)
