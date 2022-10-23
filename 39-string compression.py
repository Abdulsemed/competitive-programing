def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        beg = 0 
        end = 1
        s = ""
        while beg <= len(chars) - 1:
            count = 1
            while end <= len(chars)-1 and chars[beg] == chars[end]:
                count += 1
                end += 1
            s = s + chars[beg]
            if count > 1:
                s = s + str(count)
            beg = end
            if end <= len(chars)-1:
                end += 1
        chars[:] = [elt for elt in s]
        return len(chars)
