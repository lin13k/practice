import timeit

code = '''
import random
a = [(random.randint(1, 10000), random.randint(1, 10000), random.randint(1, 10000), random.randint(1, 10000)) for i in range(1000)]
sorted(a, key=lambda x: x[0])
'''

print(timeit.timeit(code, number=100))



