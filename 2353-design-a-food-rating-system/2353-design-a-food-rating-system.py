from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dicts = {}
        self.cuisine = defaultdict(SortedList)
        for index in range(len(foods)):
            self.dicts[foods[index]] = [cuisines[index],ratings[index]]
            self.cuisine[cuisines[index]].add([ratings[index], foods[index]])
    def changeRating(self, food: str, newRating: int) -> None:
        cuis = self.dicts[food][0]
        rating = self.dicts[food][1]
        self.dicts[food][1] = newRating
        self.cuisine[cuis].remove([rating,food])
        self.cuisine[cuis].add([newRating, food])
    def highestRated(self, cuisine: str) -> str:
        left = 0
        right = len(self.cuisine[cuisine])-1
        target = self.cuisine[cuisine][-1][0]
        while left<= right:
            mid = left +(right-left)//2
            if self.cuisine[cuisine][mid][0] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return self.cuisine[cuisine][left][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)