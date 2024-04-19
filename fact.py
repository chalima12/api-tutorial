from mpmath import mp
mp.dps = 50
n=int(input('enter the nuber to get factorial : '))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
fact_result=factorial(n)
digit=len(str(factorial(n)))
print(f'Factorial of {n} is {fact_result:.2e}.')
print(f'factorial of {n} is {digit} digit long')