class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        mydict = { 2:['a','b','c'],  3:['d','e','f'],  4:['g','h','i'],
                   5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],
                   8:['t','u','v'],9:['w','x','y','z'] 
                 }
        
        if(len(digits) == 0):
            return []
        else:
            l = ['no number']
            n = len(digits)
            for i in range(len(digits)):
                l.append(int(digits[i]))
        sol = [ ]
        Solution.letter_helper("",1,n,l,mydict,sol)
        
        return sol
            
        
    
    @staticmethod
    def letter_helper(mystring, cur_digit,n,l,mydict,sol):
        
        if(cur_digit>n):
            sol.append(mystring)
            
            
        else:
            
            digit = l[cur_digit]
            for i in mydict[digit]:
                Solution.letter_helper(mystring + i,cur_digit + 1, n , l, mydict,sol)
    
    
    
    
    
    
        
        
        