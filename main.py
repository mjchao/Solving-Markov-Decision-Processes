'''
Created on Nov 28, 2015

@author: mjchao
'''

import Problem1

def problem1():
    print "Solving Problem 1"
    answers = Problem1.solve()
    f = open( "generated/P1-output.txt" , "w" )
    f.write( "0.0000\n\n" )
    prevPolicyStr = str(Problem1.get_optimal_policy( 0 ))
    f.write( prevPolicyStr + "\n" )
    for i in range(0,8):
        f.write( str('{0:.4f}'.format(answers[ i ])) + "\n\n" )
        nextPolicyStr = str(Problem1.get_optimal_policy( answers[ i ] - 0.0001 ))
        output = ""
        for i in range(len(nextPolicyStr)):
            if ( nextPolicyStr[ i ] == prevPolicyStr[ i ] ):
                output += nextPolicyStr[ i ]
            else:
                output += nextPolicyStr[ i ] + "*"
                
        f.write( output + "\n" )
        prevPolicyStr = nextPolicyStr
        
    f.close()
    print "Finished Solving Problem 1"
    
problem1()