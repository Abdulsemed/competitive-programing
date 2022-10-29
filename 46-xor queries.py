def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix =[arr[0]]
        result = []
        for index in range(1, len(arr)):
            prefix.append(prefix[index-1]^arr[index])
        for index in range(len(queries)):
            l = queries[index][0]
            r = queries[index][1]
            if l != 0:
                result.append(prefix[r] ^ prefix[l-1])
            else:
                result.append(prefix[r])
        return result
