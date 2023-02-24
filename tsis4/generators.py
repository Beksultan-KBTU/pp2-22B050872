# problem 1
'''
n = int(input())
a = (int(i) ** 2 for i in range(0, n + 1))
for i in range(n + 1):
    print(next(a))
'''

# problem 2
'''
n = int(input())
a = (int(2 * i) for i in range(round(n / 2) + 1)) 
for i in range(int(n / 2)):
    print(next(a), end = ', ')
print(next(a))
'''

# problem 3
'''
n = int(input())
def divisibility(n):
    return(x for x in range(n + 1) if(x % 12 == 0))
for i in divisibility(n):
    print(i)
'''

#problem 4
'''
a = int(input())
b = int(input())
g = (int(i) ** 2 for i in range(a, b + 1))
for i in range(a, b + 1):
    print(next(g))
'''

# problem 5
'''
n = int(input())
a = (int(i) for i in range(n, -1, -1))
for i in range(n + 1):
    print(next(a))
'''