def exam(students, questions, answers, weight):
    count = 0
    for index in range(questions):
        answerDict = {}
        for val in range(students):
            answerDict[answers[val][index]] = 1 + answerDict.get(answers[val][index], 0)
        count += max(answerDict.values())*weight[index]
    
    print(count)
  
nums = list(map(int, input().split(" "))) 
answers= []
for _ in range(nums[0]):
    answers.append(input())
weight = list(map(int, input().split(" "))) 
exam(nums[0], nums[1], answers, weight)
