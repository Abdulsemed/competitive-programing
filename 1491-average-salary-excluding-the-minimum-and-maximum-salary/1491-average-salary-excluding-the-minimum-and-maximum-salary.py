class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = salary[0]
        maxSalary = salary[0]
        maxHolder = salary[0]
        minHolder = salary[0]
        average = 0
        for money in salary:
            if money > maxSalary:
                if minSalary != maxSalary:
                    average += maxSalary 
                maxSalary = money
            elif money < minSalary:
                if minSalary != maxSalary:
                    average += minSalary
                minSalary = money
            elif money < maxSalary and money > minSalary:
                average += money
            
        
        average = average/(len(salary)-2)
        return average