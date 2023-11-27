class Solution:
    def value(self,index,formula):
        curr = 0
        while index < len(formula) and formula[index].isdigit():
            curr = curr*10 + int(formula[index])
            index += 1
        return (curr,index)      
    def countOfAtoms(self, formula: str) -> str:
        arr = []
        index = 0
        while index < len(formula):
            
            if formula[index].isdigit():
                curr,index = self.value(index, formula)
                if arr and arr[-1] != "(":
                    arr.append(curr)
                continue
    
            elif formula[index] == "(":
                arr.append("(")
                index+= 1
                continue
            elif formula[index] == ")":
                index += 1
                curr,index = self.value(index,formula)
                if curr == 0: curr = 1
                holder = []
                while arr[-1] != "(":
                    value = arr.pop() * curr
                    element = arr.pop()
                    holder.append(element)
                    holder.append(value)
                arr.pop()
                arr += holder
                continue
            elif formula[index].isalpha():
                arr.append(formula[index])
                index += 1
                if index < len(formula) and formula[index].isalpha() and formula[index].lower() == formula[index]:
                    arr[-1] += formula[index]
                    index += 1
                if (index < len(formula) and not formula[index].isdigit()) or index >= len(formula):
                    arr.append(1)
                continue
        dicts = {}
        for index in range(0,len(arr),2):
            dicts[arr[index]] = arr[index+1] + dicts.get(arr[index],0)
        answer = []
        arr = sorted(dicts.items())
        for key,value in arr:
            answer.append(key)
            if value > 1:
                answer.append(str(value))
        return "".join(answer)
                    
                    