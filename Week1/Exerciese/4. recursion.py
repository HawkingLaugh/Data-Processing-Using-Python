"""Enter n, use the recursion method (for example, 
derive the latter term from the relationship between the preceding items, 
it is a one-loop question) and caculate the sum of 1+2!+3!+...+n! and output the result."""

n = int(input('Give me a integer: '))
s = term = 1

for i in range(2, n+1):
    term *= i
    s += term
print(s)