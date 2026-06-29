#int 
x = input("what's x ")
y = input("What's y ")
z= x + y
print(z)
#but it not make a sum it will do a concatnaion of two input string 
# for doing the addition in we have to told the complier about the input is was a integer not the string 
x = input("what's x ")
y = input("What's y ")
z = int(x) + int(y)
print(z)
# we done this in other ways also 
x = int(input("whats'x "))
y = int(input("what's y "))
print(x+y)
# or we can write in the this way also 
print(int(input("what's x")) + int(input("what's y"))) # but i create complexity and people tends to make mistake 
#float
x = float(input("what's x "))
y = float(input("what's y"))
print(x+y)
# using round function it round the float number to the nearest integers 
x = float(input("what's x "))
y = float(input("what's y"))
z= round(x+y)
print(z)
#fromate the number 
x = float(input("what's x "))
y = float(input("what's y"))
z= round(x+y)
print(f"{z:,}")
#doing divison 
x = float(input("what's x "))
y = float(input("what's y"))
z = x / y 
print(z)
#or for rounding of 
print(f"{z:.2f}")