# looping through each value of list

nums = [1, 2, 3, 4, 5, 6]
#for num in nums:
    #print(num)

# break statment

for num in nums:
   if num == 3:
       print('Found!')
       break
   print(num)

# continue

for num in nums:
   if num == 3:
       print('Found!')
       continue
   print(num)

# loop within loop 

for num in nums:
    for letter in 'abc':
        print(num, letter)

# range()
for i in range(1, 11):
    print(i)

# while loop

x = 0
while x < 10:
    print(x)
    x += 1

# any point where you break out loop

x = 0
while x < 10:
    if x ==5:
        break
    print(x)
    x += 2

# practice while

a = 10
while a < 21:
    print(a)
    a = a + 1