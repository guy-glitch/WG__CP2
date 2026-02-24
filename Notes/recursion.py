#WG_CP2 recursion notes
#for nm in range(1,11):
 #   if nm % 2 == 0:
  #      print(nm)

#even = []

num = 3
sum =1

#for x in range(1,num+1):
 #   sum *= x
#print(sum)

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(f"Recursion {factorial(num)}")

fib = [1,1]
for i in range(1,11):
    fib.append(fib[i-1] +fib[i])

print(f"{fib} loop")


nums = []


def fibonacci(n):
    if n == 2: 
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)
print(f"{fibonacci(11)} redcursion")
