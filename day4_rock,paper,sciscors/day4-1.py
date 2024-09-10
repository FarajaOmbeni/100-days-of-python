import random

# random Integers
print(random.randint(1,10))

# random numbers from 0 to 1
print(random.random())

# random floaating numbers
print(random.uniform(1,10))
num = random.randint(0,1)
if num == 0:
    print("Heads")
else:
    print("Tails")