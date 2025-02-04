a = 5
b = 7

sum = a + b
#print(sum)

# redundent / repeatability

# redundent agar kar rehe to bad dev ho tum

# ab repeat na ho to isi liye repeat nhi 

def sum(num):
    total = num*num
    return total

#sum(6) # this is also print statement

def square(num):
   a =num*num
   return a


print(square(2))

def avg(a, b, c, d, e, f):
    sum = a + b + c + d + e + f
    avgr = sum// 6
    return avgr

cam = avg(2, 3, 5, 1, 5, 4)
print(cam)

# assign default value

def avg(a=1, b=2, c=1):
    print("bahar niklo")

print()