class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}' : '{' }
        isOpen = { '(': True, '[':True, '{' : True, ')': False, '}': False, ']': False  }
        
        
        if(len(s) == 0):
            return True
        
        if(len(s)%2 != 0 or s[0] in dic.keys()):
            return False
        
        
        l = [ ]
        for i in range(len(s)):
            if(isOpen[s[i]]):
                l.insert(0,s[i])
            else:
                if(len(l)>0 and l.pop(0) != dic[s[i]]):
                    return False
                
                
        if(len(l) == 0):
            return True
        else:
            return False
       