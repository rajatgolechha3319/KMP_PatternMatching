import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#                                                  Time complexity                   Space Complexity
def f(x,q):
#Initialisation                                                                                                       
    f_x=0                                              #O(1)                            O(1)                            
    coeff_f_x = 1                                      #O(1)                            O(1)                                     
    n = len(x)                                         #O(1)                            O(log(len(x)))  
# This functions calculates the value of f(x)%q for the given x and q
# Loop                               
    for i in range(n-1,-1,-1):                            #O(nlog(q))                       O(log(q))                                                   
        f_x += (coeff_f_x*((ord(x[i])-65)%q)%q)        #O(log(q))                       O(log(q))    
        f_x = f_x%q                                    #O(log(q))                       O(log(q))                                     
        coeff_f_x*=26                                  #O(1)                            O(log(q))                    
        coeff_f_x=coeff_f_x%q                          #O(log(q))                       O(log(q))                                                                                                                                       
    return f_x                                                                                                      
#                                        Overall:       O(len(x))                       O(log(len(x))+log(q))

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))                               #O(log(len(p)/eps)^2)           O(log(m/eps))
# Since n>log(m/eps) , we can write Tc as O(nlog(m/eps)) also... 
                                                                            
	q = randPrime(N)                                                                                                                        
	return modPatternMatch(q,p,x)   # Now log(q) is of order log(m/eps) therefore   
#Overall Tc = O(n log(m/eps)) and overall Space complexity is k +log(n) +log(m/eps)                                                                                              


#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))                              #O(log(len(p)/eps)^2)           O(log(m/eps))
# Since n>log(m/eps) , we can write Tc as O(nlog(m/eps)) also...

	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)   # Now log(q) is of order log(m/eps) therefore  
#Overall Tc = O(n log(m/eps)) and overall Space complexity is k +log(n) +log(m/eps)

# return appropriate N that satisfies the error bounds
def findN(eps,m):    
# To find a suitable N to satisfy the given error range and improve the complexity
                                                                                              
    target = 2*(m/eps)*(math.log2(26))                  #O(log(m/eps))                  O(log(m/eps))   
# The value to achieve;
#This functions reports our distance from the target with sign
                                                           
    def g(x,y):                                             #O(log(m/eps)) in our case x,y are both O(m/eps), O(log(m/eps))                                                        
        z = (y-(x/math.log2(x)))                        #O(log(x)+log(y))               O(log(m/eps))                                                             
        return z                                        #O(1)                                                            
    prev = target                                       #O(1)                           O(log(m/eps))                                 
    next = target*target                                #O(1)                           O(log(m/eps)) 
# reach close to the target from both sides                                        
    while(g(prev,target)>0):                                #O(log(m/eps))                  O(log(m/eps))                                                          
        prev *=2                                        #O(1)                           O(log(m/eps))                                 
    while(g(next,target)<0):                                #O(log(m/eps))                  O(log(m/eps))                                                          
        next /=2                                        #O(1)                           O(log(m/eps))                                 
    prev,next = next,prev                               #O(1)
# Now that you have two values on both sides do a binary search by halving the interval every time...                                                                   
    while ((abs(g(prev,target))/target>0.001) and (abs(g(next,target))/target>0.001) and (next-prev)>1):  #log(m/eps)^2  , O(log(m/eps))                                                                                                    
        mid = (prev+next)/2                             #O(1)                           O(log(m/eps))                                          
        if g(mid,target)>0:                             #O(log(m/eps))                  O(log(m/eps))                                                   
            next = mid                                  #O(1)                           O(log(m/eps))                                      
        else:                                                                                                   
            prev = mid                                  #O(1)                           O(log(m/eps))                                      
    if abs(g(prev,target))/target<0.001:                #O(log(m/eps))                  O(log(m/eps))                                                                   
        return int(prev)                                                                          
    else:                                                                                                  
        return int(next)                                
#                                   Overall:            O(log(m/eps)^2)                 O(log(m/eps)) 
                                        

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
# Initialisation
    Key = f(p,q)                                        #O(len(p))                      O(log(m)+log(q))                                      
    m = len(p)                                          #O(1)                           O(log(m))                             
    n = len(x)                                          #O(1)                           O(log(n))                             
    coeff_fx_0 = 1                                      #O(1)                           O(1)       
# We need the value of 26^m % q, hence the loop                      
    for i in range(m-1):                                    #O(m-1)                         O(log(q))                                           
        coeff_fx_0 = (coeff_fx_0*26)%q                  #O(log(q))                      O(log(q))                                                                                                                         
    Output_list = []                                    #O(1)                           O(1)                                     
    base_case = f(x[0:m],q)                             #O(m)                           O(log(m)+log(q))                                         
    if base_case == Key:                                #O(1)                                                                    
        Output_list.append(0)                           #O(1)                           O(1)                                             
    old_output = base_case                              #O(1)                           O(log(m)+log(q))  
# Now we iterate over the string adding and removing the bits from rear and front to achieve our purpose of obtaining the value of
# f for all substrings and then match them with the key we have and report if True...                                 
    for i in range(1,n-m+1):                                #O(n-m)*log(q)                   O(log(q))                                               
        alpha = old_output - (coeff_fx_0*((ord(x[i-1])-65)%q))%q  #O(log(q))            O(log(q))                                                                                      
        alpha = alpha%q                                 #O(log(q))                      O(log(q))                                          
        alpha = (alpha*(26%q))%q                        #O(log(q))                      O(log(q))                                                      
        alpha = alpha + ((ord(x[i+m-1])-65)%q)          #O(log(q))                      O(log(q))                                                                  
        alpha = alpha%q                                 #O(log(q))                      O(log(q))                                          
        if alpha == Key:                                #O(log(q))                                                                    
            Output_list.append(i)                       #O(1)                           O(1)                                                 
        old_output = alpha                              #O(1)                      O(log(q))                                              
        
    return Output_list
#                                       Overall:        O(nlog(q))                      O(k+log(n)+log(q))

#                                                  Time complexity                   Space Complexity
def g(x,q):                                                                                            
# Initialisation           
    f_x=0                                              #O(1)                            O(1) 
    IndiceKeyList =[]                                  #O(1)                            O(1)
    coeff_f_x = 1                                      #O(1)                            O(1)                                     
    n = len(x)                                         #O(1)                            O(log(len(x)))   
#This function finds the value of the f(x)%q for the wildcard
#Loop                              
    for i in range(n-1,-1,-1):                            #O(nlog(q))                       O(log(q))      
        if x[i]!="?":                                             
            f_x += (coeff_f_x*((ord(x[i])-65)%q)%q)    #O(log(q))                       O(log(q))   
        else:
            f_x +=0
            IndiceKeyList.append(i)                    #O(1)                            O(1) 
            IndiceKeyList.append(coeff_f_x)            #O(1)                            O(1) 
        f_x = f_x%q                                    #O(log(q))                       O(log(q))                                     
        coeff_f_x*=26                                  #O(1)                            O(log(q))                    
        coeff_f_x=coeff_f_x%q                          #O(log(q))                       O(log(q)) 
                                                                                                                                              
    return f_x,IndiceKeyList                                                                                                      
#                                        Overall:       O(len(x))                       O(log(len(x))+log(q))

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
# Initialisation
    Key,IndiceKeylist = g(p,q)                          #O(len(p))                      O(log(m)+log(q))  
    index = IndiceKeylist[0]                            #O(1)                           O(1)
    key_index = IndiceKeylist[1]                        #O(1)                           O(1)                                    
    m = len(p)                                          #O(1)                           O(log(m))                             
    n = len(x)                                          #O(1)                           O(log(n))                             
    coeff_fx_0 = 1                                      #O(1)                           O(1)  
# We need the value of 26^m % q, hence the loop                             
    for i in range(m-1):                                    #O(m-1)                         O(log(q))                                           
        coeff_fx_0 = (coeff_fx_0*26)%q                  #O(log(q))                      O(log(q))                                                                                                                         
    Output_list = []                                    #O(1)                           O(1)                                     
    base_case = f(x[0:m],q)                             #O(m)                           O(log(m)+log(q))                                         
    if(base_case-((ord(x[index])-65)%q)*key_index)%q == Key:#O(log(q))                                                                    
        Output_list.append(0)                           #O(1)                           O(1)                                             
    old_output = base_case                              #O(1)                           O(log(m)+log(q))
# Now we iterate over the string adding and removing the bits from rear and front to achieve our purpose of obtaining the value of
# f for all substrings and then match them with the key we have and report if True...                                            
    for i in range(1,n-m+1):                              #O(n-m)*log(q)                   O(log(q))                                               
        alpha = old_output - (coeff_fx_0*((ord(x[i-1])-65)%q))%q  #O(log(q))            O(log(q))                                                                                      
        alpha = alpha%q                                 #O(log(q))                      O(log(q))                                          
        alpha = (alpha*(26%q))%q                        #O(log(q))                      O(log(q))                                                      
        alpha = alpha + ((ord(x[i+m-1])-65)%q)          #O(log(q))                      O(log(q))                                                                  
        alpha = alpha%q                                 #O(log(q))                      O(log(q))  
        beta = (alpha - ((ord(x[index+i])-65)%q)*key_index)%q #O(log(q))                O(log(q))                                       
        if beta == Key:                                 #O(log(q))                                                                    
            Output_list.append(i)                       #O(1)                           O(1)                                                 
        old_output = alpha                              #O(1)                      O(log(q))                                              
        
    return Output_list
#                                       Overall:        O(nlog(q))                      O(k+log(n)+log(q))
