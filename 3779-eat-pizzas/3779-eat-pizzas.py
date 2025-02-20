class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        days = (len(pizzas)//4)
        sums = 0
        odd = math.ceil((len(pizzas)/4)/2)
        index = len(pizzas)-1
        while days:
            if odd:
                sums += pizzas[index]
                odd -= 1
            else:
                index -= 1
                sums += pizzas[index]
            index -= 1
            days -= 1
        return sums
        