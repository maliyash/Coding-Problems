class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        i = 0
        j= 0
        my_set = set([])
        #my_set.remove(2)
        max_len = 0
        #s = "xyzypqr"
        
        
        while(j<len(s)):
            
            if(s[j] not in my_set):
                my_set.add(s[j])
                j = j + 1
                count = j - i
                if(max_len < count):
                    max_len = count
            
            else:
                while(s[i] != s[j]):
                    my_set.remove(s[i])
                    i = i + 1;
                my_set.remove(s[i])
                i = i + 1
                
        
        
        return max_len

