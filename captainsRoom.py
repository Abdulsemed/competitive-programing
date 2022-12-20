def func(k, nums):
    rooms = {}
    for val in nums:
        rooms[val] = 1 + rooms.get(val,0)
    for val in rooms.keys():
        if rooms[val] == 1:
            print(val)
            break
    
size = int(input())
num = input()
nums = num.split(" ")
func(size, nums)
