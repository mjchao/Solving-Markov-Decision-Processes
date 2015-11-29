'''
Created on Nov 28, 2015

@author: mjchao
'''

class Policy( object ):
    
    def __init__( self ):
        self._actions = [['?' for _ in range(0,4)] for _ in range(0,3)]
        self._actions[ 1 ][ 1 ] = 'X'
        self._actions[ 0 ][ 3 ] = '1'
        self._actions[ 1 ][ 3 ] = '-1' 
        
    def __str__( self ):
        rtn = ""
        for i in range( 0 , 3 ):
            rtn += str( self._actions[ i ][ 0 ] ) + " " + str( self._actions[ i ][ 1 ] ) + " " + \
                    str( self._actions[ i ][ 2 ] ) + " " + str( self._actions[ i ][ 3 ] ) + "\n"
        return rtn
'''
Note: Because the assignment uses he environment shown in
Figure 17.1 of Artificial Intelligence: A Modern Approach,
the dimensions will be hard coded as 3-by-4
'''

class UtilityMap( object ):
    
    def __init__( self ):
        self._utilities = [[0 for _ in range(0,4)] for _ in range(0,3)]
        
    def __str__( self ):
        rtn = ""
        for i in range(0, 3):
            rtn += str( self._utilities[ i ][ 0 ] ) + " " + str( self._utilities[ i ][ 1 ] ) + " " + \
                 str( self._utilities[ i ][ 2 ] ) + " " + str( self._utilities[ i ][ 3 ] ) + "\n"
        return rtn
    
    def get_optimal_policy(self):
        self._policy = Policy()
        dRow = [ 1 , 0 , -1 , 0 ]
        dCol = [ 0 , 1 , 0 , -1 ]
        direction = [ '>' , '^' , '<' ,'V' ]
        for row in range( 0 , 3 ):
            for col in range( 0 , 4 ):
                
                #ignore the invalid square on the map
                if col == 1 and row == 1:
                    continue
                bestUtility = self._utilities[ row ][ col ]
                self._policy._actions[ row ][ col ] = '-'
                
                for i in range( 0 , 4 ):
                    newCol = col + dRow[ i ]
                    newRow = row + dCol[ i ]
                    
                    #ignore the invalid square on the map
                    if ( newCol == 1 and newRow == 1 ):
                        continue
                    
                    #calculate the best direction in which to move
                    if ( 0 <= newCol and newCol <= 3 and 0 <= newRow and newRow <= 2):
                        if ( self._utilities[ newRow ][ newCol ] > bestUtility ):
                            bestUtility = self._utilities[ newRow ][ newCol ]
                            self._policy._actions[ row ][ col ] = direction[ i ]
                            
        return self._policy
        
def apply_value_iteration( map ):        
    pass
        
def main():
    map = UtilityMap()
    apply_value_iteration( map )
    print map
    print map.get_optimal_policy()

if __name__ == "__main__": main()