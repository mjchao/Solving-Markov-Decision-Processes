'''
Created on Nov 29, 2015

@author: mjchao
'''

import copy

NORTH = '^'
SOUTH = 'V'
EAST = '>'
WEST = '<'
STAY = '-'

class RewardSet( object ):
    
    def __init__( self ):
        pass
    
    def get_reward( self , row , col ):
        if ( row == 0 and col == 0 ):
            return 3
        if ( row == 0 and col == 2 ):
            return 10
        return -1
    
class TransitionModel( object ):
    
    def __init__( self ):
        pass
    
    def get_transition_probability( self , destination , curr , action ):
        destRow = destination[ 0 ]
        destCol = destination[ 1 ]
        currRow = curr[ 0 ]
        currCol = curr[ 1 ]
        
        #terminal state (positive)
        if ( currRow == 0 and currCol == 2 ):
            return 0
        
        northRow = max( 0 , currRow-1 )
        northCol = currCol
            
        southRow = min( 2 , currRow+1 )
        southCol = currCol
        
        eastRow = currRow
        eastCol = min( 2 , currCol+1 )
        
        westRow = currRow
        westCol = max( 0 , currCol-1 )
        
        rtn = 0
        if ( action == NORTH ):
            if ( northRow == destRow and northCol == destCol ):
                rtn += 0.8
            if ( eastRow == destRow and eastCol == destCol ):
                rtn += 0.1
            if ( westRow == destRow and westCol == destCol ):
                rtn += 0.1
        elif ( action == SOUTH ):
            if ( southRow == destRow and southCol == destCol ):
                rtn += 0.8
            if ( eastRow == destRow and eastCol == destCol ):
                rtn += 0.1
            if ( westRow == destRow and westCol == destCol ):
                rtn += 0.1
        elif ( action == EAST ):
            if ( eastRow == destRow and eastCol == destCol ):
                rtn += 0.8
            if ( northRow == destRow and northCol == destCol ):
                rtn += 0.1
            if ( southRow == destRow and southCol == destCol ):
                rtn += 0.1
        elif ( action == WEST ):
            if ( westRow == destRow and westCol == destCol ):
                rtn += 0.8
            if ( northRow == destRow and northCol == destCol ):
                rtn += 0.1
            if ( southRow == destRow and southCol == destCol ):
                rtn += 0.1
            
        return rtn
    
class Policy( object ):
    
    def __init__( self ):
        self._actions = [['?' for _ in range(0,3)] for _ in range(0,3)]
        self._actions[ 0 ][ 2 ] = '10'
        
    def __str__( self ):
        self._actions[ 0 ][ 2 ] = '10'
        rtn = ""
        for i in range( 0 , 3 ):
            rtn += str( self._actions[ i ][ 0 ] ) + " " + str( self._actions[ i ][ 1 ] ) + " " + \
                    str( self._actions[ i ][ 2 ] ) + "\n"
        return rtn
    
    def __eq__( self , other ):
        return str(self) == str(other)
    
    def __ne__( self , other ):
        return str(self) != str(other)
    
    
class UtilityMap( object ):
    
    def __init__( self ):
        self._utilities = [[0 for _ in range(0,3)] for _ in range(0,3)]
        
        
    def __str__( self ):
        rtn = ""
        utilities = [['0' for _ in range(0,3)] for _ in range(0,3)]
        for i in range(0,3):
            for j in range(0,3):
                utilities[ i ][ j ] = '{0:.3f}'.format( self._utilities[ i ][ j ] ) 
        for i in range(0, 3):
            rtn += str( utilities[ i ][ 0 ] ) + " " + str( utilities[ i ][ 1 ] ) + " " + \
                 str( utilities[ i ][ 2 ] ) + "\n"
        return rtn
    
    def get_optimal_policy( self , transitionModel ):
        self._policy = Policy()
        for row in range( 0 , 3 ):
            for col in range( 0 , 3 ):
                
                bestUtility = -9999999999
                self._policy._actions[ row ][ col ] = STAY
                
                actions = [NORTH , SOUTH , EAST , WEST]
                for a in actions:
                    actionUtility = 0
                    for nextRow in range(0, 3):
                        for nextCol in range(0, 3):
                            actionUtility += transitionModel.get_transition_probability( (nextRow,nextCol) , (row,col) , a ) * self._utilities[ nextRow ][ nextCol ]
                            
                    if ( actionUtility > bestUtility ):
                        bestUtility = actionUtility
                        self._policy._actions[ row ][ col ] = a 
                            
        return self._policy
    
        
def get_action_payoff( utilMap , curr , action , transitionModel ):
    rtn = 0
    for row in range(0,3):
        for col in range(0,3):
            rtn += transitionModel.get_transition_probability( (row,col) , curr , action ) * utilMap._utilities[ row ][ col ]
    return rtn

def apply_value_iteration( utilMap , transitionModel , rewardSet , discountFactor=1 ):
    DELTA = 0.000001        
    currUtils = copy.deepcopy( utilMap )
    
    while( True ):
        nextUtils = copy.deepcopy( currUtils )
        
        for row in range(0,3):
            for col in range(0,3):
                northPayoff = get_action_payoff(currUtils , (row,col) , NORTH, transitionModel)
                southPayoff = get_action_payoff(currUtils , (row,col) , SOUTH , transitionModel)
                eastPayoff = get_action_payoff(currUtils, (row,col) , EAST , transitionModel)
                westPayoff = get_action_payoff(currUtils, (row,col) , WEST , transitionModel)
                payoffs = [ northPayoff, southPayoff , eastPayoff , westPayoff ]
                nextUtils._utilities[ row ][ col ] = rewardSet.get_reward( row , col ) + discountFactor*max( payoffs )
        
        #test for convergence
        maxChange = 0
        for row in range(0,3):
            for col in range(0,3):
                utilityChange = abs( currUtils._utilities[ row ][ col ] - nextUtils._utilities[ row ][ col ] ) 
                if ( utilityChange > maxChange ):
                    maxChange = utilityChange
        
        if maxChange < DELTA:
            break
        
        currUtils = nextUtils
    return currUtils

def get_optimal_policy( discountFactor ):
    utilMap = UtilityMap()
    transitionModel = TransitionModel()
    rewardSet = RewardSet()
    utilMap = apply_value_iteration( utilMap , transitionModel, rewardSet , discountFactor )
    return utilMap.get_optimal_policy( transitionModel )

def get_optimal_policy_and_utility( discountFactor ):
    utilMap = UtilityMap()
    transitionModel = TransitionModel()
    rewardSet = RewardSet()
    utilMap = apply_value_iteration( utilMap , transitionModel, rewardSet , discountFactor )
    return (str(utilMap.get_optimal_policy(transitionModel)) , str(utilMap))

counter = 0
def search( low , high ):
    global counter
    if ( get_optimal_policy( low ) == get_optimal_policy( high ) ):
        return []

    rtn = []
    mid = (low+high)/2
    
    lowPolicy = get_optimal_policy( low )
    midPolicy = get_optimal_policy( mid )
    highPolicy = get_optimal_policy( high )
    
    if ( midPolicy != get_optimal_policy( mid+0.00001 ) or \
         midPolicy != get_optimal_policy( mid-0.00001 ) ):
        counter += 1
        rtn.append( mid )
        print "Found", counter, "values so far."
        
    if ( lowPolicy != midPolicy ):    
        rtn.extend( search( low , mid-0.00001 ) )
        
    if ( midPolicy != highPolicy ):
        rtn.extend( search( mid+0.00001, high ) )
        
    return rtn

def solve():
    counter = 0
    answers = search( 0.0 , 0.99 )
    answers.reverse()
    return answers  

def main():
    solve()

if __name__ == "__main__": main()
