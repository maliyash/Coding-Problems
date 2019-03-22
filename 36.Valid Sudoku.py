class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
       
        
        #Scan row wise
       
        for i in range(0,9):
            rowScan = set([])
            
            for j in range(0,9):
                
                # check if the element is not '.'
                if(board[i][j] != '.'):
                    
                    #if the element is not the set add it
                    if(board[i][j] not in rowScan):
                        rowScan.add(board[i][j])
                        
                    #if the element is already in the set return False    
                    else:
                        return False
        
        
        #Scan Column Wise
        
        for j in range(0,9):
            colScan = set([])
            
            for i in range(0,9):
                
                if(board[i][j] != '.'):
                    if(board[i][j] not in colScan):
                        colScan.add(board[i][j])
                    else:
                        return False
        
        
        #Scan each 3*3 matrix
        
        mat_one = set([])
        mat_two = set([])
        mat_three = set([])
        
        
        
        # Scan first 3 row matrix
        for i in range(0,3):
            
            
            for j in range(0,3):
                
                if(board[i][j] != '.'):
                    if(board[i][j] not in mat_one):
                        mat_one.add(board[i][j])
                    else:
                        return False
                
                if(board[i][j+3] != '.'):
                    if(board[i][j+3] not in mat_two):
                        mat_two.add(board[i][j+3])
                    else:
                        return False
                    
                if(board[i][j+6] != '.'):
                    if(board[i][j+6] not in mat_three):
                        mat_three.add(board[i][j+6])
                    else:
                        return False
        
        
        
        mat_one.clear()
        mat_two.clear()
        mat_three.clear()
        
        # Scan Second 3 row matrix
        for i in range(3,6):
            
            
            for j in range(0,3):
                
                if(board[i][j] != '.'):
                    if(board[i][j] not in mat_one):
                        mat_one.add(board[i][j])
                    else:
                        return False
                
                if(board[i][j+3] != '.'):
                    if(board[i][j+3] not in mat_two):
                        mat_two.add(board[i][j+3])
                    else:
                        return False
                if(board[i][j+6] != '.'):
                    if(board[i][j+6] not in mat_three):
                        mat_three.add(board[i][j+6])
                    else:
                        return False
        mat_one.clear()
        mat_two.clear()
        mat_three.clear()
        
        #Scan third 3 row matrix
        for i in range(6,9):
            
            
            for j in range(0,3):
                
                if(board[i][j] != '.'):
                    if(board[i][j] not in mat_one):
                        mat_one.add(board[i][j])
                    else:
                        return False
                
                if(board[i][j+3] != '.'):
                    if(board[i][j+3] not in mat_two):
                        mat_two.add(board[i][j+3])
                    else:
                        return False
                if(board[i][j+6] != '.'):
                    if(board[i][j+6] not in mat_three):
                        mat_three.add(board[i][j+6])
                    else:
                        return False
        
        
        
        
        # If all checks are done return True
        
        return True