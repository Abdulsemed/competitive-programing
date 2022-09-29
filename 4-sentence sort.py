class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s=s.split(" ")
        result=""
        num_arr = [int(word[len(word)-1]) for word in new_s]
        
        for val in num_arr:
            for i in range(len(new_s)-1):
                if num_arr[i] > num_arr[i+1]:
                    holder = num_arr[i]
                    str_holder = new_s[i]
                    num_arr[i] = num_arr[i+1]
                    new_s[i] = new_s[i+1]
                    num_arr[i+1] = holder
                    new_s[i+1] = str_holder

        new_s = ' '.join([word.replace(str(index+1), "") for index, word in enumerate(new_s)])
        return(new_s)
