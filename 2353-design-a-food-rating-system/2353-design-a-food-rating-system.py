from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dicts = {}
        self.cuisine = defaultdict(list)
        for index in range(len(foods)):
            self.dicts[foods[index]] = [cuisines[index],-ratings[index]]
            heapq.heappush(self.cuisine[cuisines[index]],[-ratings[index], foods[index]])
    def changeRating(self, food: str, newRating: int) -> None:
        cuis = self.dicts[food][0]
        self.dicts[food][1] = -newRating
        heapq.heappush(self.cuisine[cuis],[-newRating, food])
    def highestRated(self, cuisine: str) -> str:
        while self.cuisine[cuisine][0][0] != self.dicts[self.cuisine[cuisine][0][1]][1]:
            heapq.heappop(self.cuisine[cuisine])
        return self.cuisine[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)