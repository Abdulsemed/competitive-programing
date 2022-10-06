def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        p_count = {}
        s_count = {}
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i],0)
        index_arr = [0] if p_count == s_count else []
        beg = 0
        for end in range(len(p), len(s)):
            s_count[s[end]] = 1 + s_count.get(s[end], 0)
            s_count[s[beg]] -= 1

            if s_count[s[beg]] == 0:
                s_count.pop(s[beg])
            beg += 1
            if s_count == p_count:
                index_arr.append(beg)
        return index_arr
