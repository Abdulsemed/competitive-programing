def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        beg = 0
        end = 0
        max_length = 0
        holder = []

        while beg < len(s) and end < len(s):
            if s[end] not in holder:
                holder.append(s[end])
                end += 1
                max_length = max(max_length, end-beg)
            else:
                holder.remove(s[beg])
                beg += 1

        return max_length
