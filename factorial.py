#!/usr/bin/python3

def iterativeFactorial(n):
    answer = 1
    for i in range(1, n+1, 1):
        answer = answer * i
    return answer

#print(iterativeFactorial(5))

def recursiveFactorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)
    
#print(recursiveFactorial(5))
#the limit is 995