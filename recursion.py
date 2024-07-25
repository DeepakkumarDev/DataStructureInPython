def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

# recursiveMethod(5)

def powerOfTwo(n):
    if n==0:
        return 1
    else:
        power=powerOfTwo(n-1)
        return power*2
def powerOfTwoItr(n):
    i=0
    power=1
    while i<n:
        power=power*2
        i+=1
    return power

# print(powerOfTwoItr(3),'iterative method')
# print(powerOfTwo(3))

def factorial(n):
    assert n>=0 and int(n)==n,'the number must be positive integer only'
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
    
# print(factorial(5))

def fibonacci(n):
    assert n>=0 and int(n)==n, 'Fibonacci number cannot be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
# print(fibonacci(6))

def sumOfDigits(n):
    assert n>=0 and int(n)==n ,'The number has to be positive integer only'
    if n==0:
        return 0
    return int(n%10)+sumOfDigits(int(n/10))

# print(sumOfDigits(124))

def power(base,exp):
    assert exp>=0 and int(exp)==exp,'The exponent must be positive integer only'
    if exp==0:
        return 1
    if exp==1:
        return base
    return base*power(base,exp-1)

# print(power(3,3))


def gcd(a,b):
    assert int(a)==a and int(b)==b,'The numbser must be integer only'
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    else:
        return gcd(b,a%b)

# print(gcd(8,4))


def decimalToBinary(n):
    assert int(n)==n,'The parameter must be an integer only!'
    if n==0:
        return 0
    return n%2 +10*decimalToBinary(int(n/2))
    
# print(decimalToBinary(3))


def capitalizeWords(arr):
    result=[]
    if len(arr)==0:
        return result 
    result.append(arr[0].upper())
    return result +capitalizeWords(arr[1:])

words=['i','am','learning','recursion']
# print(capitalizeWords(words))


def sum(n):
    if n<=0:
        return 0
    else:
        return n+sum(n-1)
    
# print(sum(3))

def pairSumSequence(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+pairSum(i,i+1)
    return sum

def pairSum(a,b):
    return a+b

# print(pairSumSequence(3))


def findBiggestNumber(sampleArray):
    biggestNumber=sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index]>biggestNumber:
            biggestNumber=sampleArray[index]
    print(biggestNumber)

# findBiggestNumber([1,2,4,5])


def findMaxNumRec(sampleArray,n):
    if n==1:
        return sampleArray[0]
    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))



def allFib(n):
    for i in range(n):
        print(str(i)+" :, "+str(fib(i)))

def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

# allFib(7)

def powersOf2(n):
    if n<1:
        return 0
    elif n==1:
        print(1)
        return 1
    else:
        prev=powersOf2(int(n/2))
        curr=prev*2
        print(curr)
        return curr
    
powersOf2(4)