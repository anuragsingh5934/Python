# using random module in py 
import random

for i in range(3):
    print(random.randint(10, 20))

# random picking from a list

members = ['john', 'mary', 'bob', 'mosh']
leader = random.choice(members)
print(leader)