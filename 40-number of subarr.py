def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        beg = 0
        end = k
        counter = 0
        avg = sum(arr[beg:end])
        while end <= len(arr):
            if avg/k >= threshold:
                counter += 1
            if end <= len(arr) - 1:
                avg += (arr[end] - arr[beg])
            end += 1
            beg += 1
        return counter
