'''
Created on Nov 28, 2015

@author: mjchao
'''

import Problem1
from Problem1 import UtilityMap, Policy , TransitionModel , RewardSet , NORTH , SOUTH , EAST , WEST , STAY

import random
import numpy

def is_terminal_state( stateRow , stateCol ):
    if stateRow == 0 and stateCol == 3:
        return True
    if stateRow == 1 and stateCol == 3:
        return True
    return False 

def get_move_direction( direction ):
    randMoveVal = random.random()
    if ( direction == NORTH ):
        if ( randMoveVal < 0.8 ):
            return NORTH
        elif( randMoveVal < 0.9 ):
            return EAST
        else:
            return WEST
    elif( direction == SOUTH ):
        if ( randMoveVal < 0.8 ):
            return SOUTH
        elif( randMoveVal < 0.9 ):
            return EAST
        else:
            return WEST
    elif( direction == EAST ):
        if ( randMoveVal < 0.8 ):
            return EAST
        elif( randMoveVal < 0.9 ):
            return NORTH
        else:
            return SOUTH
    elif( direction == WEST ):
        if ( randMoveVal < 0.8 ):
            return WEST
        elif( randMoveVal < 0.9 ):
            return NORTH
        else:
            return SOUTH
        
    raise "Invalid move direction"

def make_move( currRow , currCol , direction ):
    nextRow = -1
    nextCol = -1
    if ( direction == NORTH ):
        nextRow = max( 0 , currRow-1 )
        nextCol = currCol
    elif( direction == SOUTH ):
        nextRow = min( 2 , currRow+1 )
        nextCol = currCol
    elif( direction == EAST ):
        nextRow = currRow
        nextCol = min( 3 , currCol+1 )
    elif( direction == WEST ):
        nextRow = currRow
        nextCol = max( 0 , currCol-1 )
    else:
        raise "Invalid move direction"
    
    #cannot move onto the X
    if ( nextRow == 1 and nextCol == 1 ):
        return (currRow , currCol)
    else:
        return (nextRow , nextCol)

def simulate_run( startRow , startCol , policy , rewardSet ):
    currRow = startRow
    currCol = startCol
    reward = rewardSet.get_reward( currRow , currCol )
    while( not is_terminal_state( currRow , currCol ) ):
        optimalDirection = policy._actions[ currRow ][ currCol ]
        moveDirection = get_move_direction( optimalDirection )
        newSquare = make_move( currRow , currCol , moveDirection )
        currRow = newSquare[ 0 ]
        currCol = newSquare[ 1 ]
        reward += rewardSet.get_reward( currRow , currCol )
    return reward
        

def apply_monte_carlo_simulation( costOfLiving , numTimes ):
    utilMap = UtilityMap()
    transitionModel = TransitionModel()
    rewardSet = RewardSet( costOfLiving )
    utilMap = Problem1.apply_value_iteration( utilMap , transitionModel , rewardSet )
    policy = utilMap.get_optimal_policy( transitionModel )
   
    rewards = []
    for _ in range( numTimes ):
        rewards.append( simulate_run( 2 , 3 , policy , rewardSet ) ) 
    return rewards
    

def solve():
    utilMap = UtilityMap()
    transitionModel = TransitionModel()
    rewardSet = RewardSet( -0.04 )
    utilMap = Problem1.apply_value_iteration( utilMap , transitionModel , rewardSet )
    
    rewards10 = apply_monte_carlo_simulation( -0.04 , 10 )
    print "10 run mean:", sum( rewards10 ) / 10.0
    print "10 run stddev:" , numpy.std( numpy.array( rewards10 ) )
    rewards100 = apply_monte_carlo_simulation( -0.04 , 100 )
    print "100 run mean:" , sum( rewards100 ) / 100.0
    print "100 run stddev:" , numpy.std( numpy.array( rewards100 ) )
    rewards1000 = apply_monte_carlo_simulation( -0.04 , 1000 )
    print "1000 run mean:" , sum( rewards1000 ) / 1000.0
    print "1000 run stddev:" , numpy.std( numpy.array( rewards1000 ) )
    return (utilMap , rewards10 , rewards100 , rewards1000)

def main():
    solve()

if __name__ == "__main__": main()