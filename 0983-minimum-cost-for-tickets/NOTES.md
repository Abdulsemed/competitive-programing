class Solution:
def mincostTickets(self, days: List[int], costs: List[int]) -> int:
size = len(days)
dp = [float("inf")]*(size)
dp[-1] = min(costs)
for index in range(size-2,-1,-1):
for val in range(3):
left = index
right = size-1
if val == 0:
target = days[left] + 0
elif val == 1:
target = days[left] + 6
else:
target = days[left] + 29
​
while left <= right:
mid = left + (right-left)//2
if days[mid] > target:
right = mid - 1
elif days[mid] < target:
left = mid + 1
else:
left = mid
break
leftCount = 0
if left < size and days[left] <= target:
left += 1
if left < size:
leftCount = dp[left]
dp[index] = min(dp[index], costs[val] + leftCount)
return dp[0]