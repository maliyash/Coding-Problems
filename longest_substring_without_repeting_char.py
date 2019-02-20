class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        i = 0
        j= 0
        # Define an empty set
        my_set = set([])
        
        # Variable to store longest substring length
        max_len = 0
        
        
        # Until we reach end of the string perform the below operations
        while(j<len(s)):
            
            # if jth element of s is not in myset then add it to set, inc j and update max_len if required 
            if(s[j] not in my_set):
                my_set.add(s[j])
                j = j + 1
                count = j - i
                if(max_len < count):
                    max_len = count
            
            # if jth element is in my_set then remove all elements in set until s[i] == s[j]
            else:
                while(s[i] != s[j]):
                    my_set.remove(s[i])
                    i = i + 1;
                # Now also remove the element k ie s[i] == s[j]     
                my_set.remove(s[i])
                i = i + 1
                
        
        # return the max_len
        return max_len

