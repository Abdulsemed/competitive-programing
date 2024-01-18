class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        count_arr = [0] * (n + 1)
        for index in range(len(bookings)):
            count_arr[bookings[index][0]-1] += bookings[index][2]
            count_arr[bookings[index][1]] -= bookings[index][2]
        for index in range(n):
            count_arr[index+1] +=count_arr[index]
        count_arr.pop()
        return count_arr
        
        