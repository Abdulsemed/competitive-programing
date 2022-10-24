def partitionLabels(self, s: str) -> List[int]:
        beg = 0
        end = len(s)-1
        result = []
        while beg <= len(s) - 1:
            while s[beg] != s[end]:
                end -= 1
            index = 1
            while index+end <= len(s)-1:
                if s[index+end] in s[beg:end]:
                    end += index
                    index = 0
                index += 1
            end += 1
            result.append(len(s[beg:end]))
            beg = end
            end = len(s)-1

        return result
