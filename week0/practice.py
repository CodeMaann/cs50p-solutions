print("hello, world")
name= input("what is your name ")
print("hello, ")
print(name)
# let's overide the new line in print fuction 
print("hello, " , end="")
print(name)
# we can also add many thing in the end 
print("hello, ", end="???")
print(name)
#using "" inside of print statement 
print('hello ,', end='"friend"')
print('')
#using escape character - \ 
print("hello ,", end="\"friend\"" ) 
print()
# using format in the string- f 
print(f"hello, {name}")
print()
#remove whitespace from string 
name= name.strip()
print(f"hello, {name} ")
# capitalize the string 
name= name.capitalize()
print(f"hello, {name}")
