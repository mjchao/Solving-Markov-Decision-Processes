'''
Created on Nov 28, 2015

@author: mjchao
'''

import Problem1, Problem2

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
    
def problem2():
    print "Solving Problem 2"
    answers = Problem2.solve()
    
    utilMap = answers[ 0 ] 
    with open( "generated/P2-output.txt" , 'w' ) as f:
        f.write( str(utilMap) + "\n" )
        
    distribution10 = answers[ 1 ]
    with open( "generated/P2-data-10.txt" , 'w' ) as f:
        for i in range(0, len(distribution10) ):
            f.write( str(distribution10[ i ]) + "\n" )
            
    distribution100 = answers[ 2 ]
    with open( "generated/P2-data-100.txt" , 'w' ) as f:
        for i in range(0, len(distribution100) ):
            f.write( str(distribution100[ i ]) + "\n" )
            
    distribution1000 = answers[ 3 ]
    with open( "generated/P3-data-1000.txt" , 'w' ) as f:
        for i in range(0, len(distribution1000) ):
            f.write( str(distribution1000[ i ]) + "\n" )
            
    print "Finished Solving Problem 2"

#problem1()
problem2()
print