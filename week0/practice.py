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
name= name.title()
#Remove the whitespace and capitLIZE 
name = name.strip().title()
# there is another method which can do all of this in single line 
name1 = input("what's your name ").strip().title()
# now we slpil user  name into first name and second name 
first, second  = name.split(" ")
print(f"hello, {first}") 
print(f"hello, {second}")
#now going to the function we can create our own function also by using def ( or we say define)
def hello():
    print("hello")
#or 
def helloo(to):
    print("hello, ", to)
name = input("what's your name ")
hello(name)
#you can also asgin the defualt value to the argument 
def helllo(to = "david"):
    print("what's your name ", to)

# today is the hoilday so no work just learning the maths 

