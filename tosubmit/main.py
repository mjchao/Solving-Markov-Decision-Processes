'''
Created on Nov 28, 2015

@author: mjchao
'''

def problem1():
    import Problem1
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
    import Problem2
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
    with open( "generated/P2-data-1000.txt" , 'w' ) as f:
        for i in range(0, len(distribution1000) ):
            f.write( str(distribution1000[ i ]) + "\n" )
            
    print "Finished Solving Problem 2"
    
def problem2_graph():
    import matplotlib.pyplot as plt
    import numpy
    data = []
    with open( "generated/P2-data-10.txt" , 'r' ) as f:
        for line in f.readlines():
            data.append( float(line) )
        
    plt.hist( numpy.asarray( data , dtype='float' ) , bins=100 , normed=True )
    plt.xlabel( "Reward" )
    plt.ylabel( "Count" )
    plt.title( "Number of Runs with Given Reward" )
    plt.show()
    
def problem2_mean_stddev():
    import numpy
    data = []
    with open( "generated/P2-data-10.txt" , 'r' ) as f:
        for line in f.readlines():
            data.append( float(line) )
    data = numpy.array( data )
    print "10 run mean:" , numpy.mean( data )
    print "10 run stddev:" , numpy.std( data )
    
    data = []
    with open( "generated/P2-data-100.txt" , 'r' ) as f:
        for line in f.readlines():
            data.append( float(line) )
    data = numpy.array( data )
    print "100 run mean:" , numpy.mean( data )
    print "100 run stddev:" , numpy.std( data )
    
    data = []
    with open( "generated/P2-data-1000.txt" , 'r' ) as f:
        for line in f.readlines():
            data.append( float(line) )
    data = numpy.array( data )
    print "1000 run mean:" , numpy.mean( data )
    print "1000 run stddev:" , numpy.std( data )
    
    
def problem3():
    import Problem3
    print "Solving Problem 3"
    answers = Problem3.solve()
    #answers = [0.9710211215209961, 0.8770586520385741, 0.8597617022705077, 0.8598523413085937, 0.7330785400390625]
    #print answers
    
    f = open( "generated/P3-output.txt" , "w" )
    f.write( "0.99000\n\n" )
    outputData = Problem3.get_optimal_policy_and_utility( 0.99 - 0.00001 )
    prevPolicyStr = outputData[ 0 ]
    f.write( prevPolicyStr + "\n" )
    utilityOutput = outputData[ 1 ]
    f.write( utilityOutput + "\n" )
    
    for i in range(0,len(answers)):
        f.write( str('{0:.5f}'.format(answers[ i ])) + "\n\n" )
        outputData = Problem3.get_optimal_policy_and_utility( answers[ i ] - 0.00001 )
        nextPolicyStr = outputData[ 0 ]
        policyOutput = ""
        for i in range(len(nextPolicyStr)):
            if ( nextPolicyStr[ i ] == prevPolicyStr[ i ] ):
                policyOutput += nextPolicyStr[ i ]
            else:
                policyOutput += nextPolicyStr[ i ] + "*"
                
        f.write( policyOutput + "\n" )
        utilityOutput = outputData[ 1 ]
        f.write( utilityOutput + "\n" )
        prevPolicyStr = nextPolicyStr
        
    f.close()
    print "Finished Solving Problem 3"

problem1()
problem2()
problem3()
#problem2_graph()
#problem2_mean_stddev()
print