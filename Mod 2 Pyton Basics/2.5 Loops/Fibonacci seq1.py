from functools import lru_cache



@lru_cache(maxsize = 1000)
def fibonacci(n):
    #check that the input is an positive integer
    if type(n) != int:
     raise TypeError("n must be positive int")
    if n <1:
      raise   ValueError("n must be positive int")

    #compute the Nth term
    if n == 1:
     return 1
    elif n == 2:
      return 2
    elif n >2:
     return fibonacci (n-1) + fibonacci(n-2)

for n in range (1,51):
    print (fibonacci(n+1)/ fibonacci(2))

