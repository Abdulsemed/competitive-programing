class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        holder = []
        stackHolder = []
        for element in s:
            if element.isdigit():
                if stackHolder:
                    stack.append(stackHolder)
                    stackHolder = []
                holder.append(element)
            elif element =="[":
                if holder: 
                    stack.append(int(''.join(holder)))
                    holder = []
                if stackHolder:
                    stack.append(stackHolder)
                    stackHolder = []
            elif element == "]":
                if stackHolder:
                    stack.append(stackHolder)
                    stackHolder = []
                val = stack.pop()
                index = -1
                while not str(stack[-1]).isdigit():
                    if index == -1:
                        val = val[::-1]
                    index -= 1
                    val += stack.pop()[::-1]
                if index != -1: val = val[::-1]
                times = stack.pop()
                stack.append(val*(times))
                
            else:
                stackHolder.append(element)
        if stackHolder: stack.append(stackHolder)
        holder = []
        for char in stack:
            holder.extend(char)
        return ''.join(holder)