from random import randint

####FUNCTIONS

def countPrime(nums):
    countPrime = 0

    for number in nums:
        if number %number == 1:
            primeCount+=1


#def primeNum(nums):
#prime = num/1 == num



###RUNNING CODE

numList = []
for x in range(100):
    num = randint(10,99)
    numList.append(num)

print (numList)
countPrime(numList)
print("Here are the prime numbers")
print(countPrime)
