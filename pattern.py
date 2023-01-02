def pattern(size, inputs):
    wordSize = len(inputs[0])
    sets = set()
    result = ""
    for index in range(wordSize):
        for val in range(size):
            if  sets and inputs[val][index] not in sets:
                if inputs[val][index] != "?":
                    sets.add(inputs[val][index])
            elif not sets and inputs[val][index] != "?":
                sets.add(inputs[val][index])
        if len(sets) == 0:
            result += "x"
        elif len(sets) == 1:
            val = list(sets)
            result += val[0]
        else:
            result += "?"
        sets = set()
            
    print(result)
 
size = int(input())
inputs = []
for _ in range(size):
    inputs.append(input())
pattern(size, inputs)
