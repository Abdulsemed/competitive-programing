 def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        if len(people) == 1 or (sum(people) <= limit and len(people) == 2):
            return 1
        else:
            people = sorted(people)
            beg = 0
            boats = 0
            end = len(people)-1
            while beg <= end:
                if people[end] == limit:
                    end -= 1
                    boats += 1
                elif beg == end:
                    boats += 1
                    end -= 1
                elif people[beg] + people[end] <= limit:
                    boats += 1
                    beg += 1
                    end -= 1
                else:
                    end -= 1
                    boats += 1
                    
        return boats
