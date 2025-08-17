
# ----- Start of chapter1\first.py -----
print("hello world")
# ----- End of chapter1\first.py -----

# ----- Start of chapter1\moduel.py -----
import pyjokes

joke = pyjokes.get_joke()
print(joke)
# ----- End of chapter1\moduel.py -----

# ----- Start of chapter1\problem1.py -----
# write the poem in pytho
print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.""")
# ----- End of chapter1\problem1.py -----

# ----- Start of chapter1\problem2.py -----
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("my name is abdul mohiz")
engine.runAndWait()
# ----- End of chapter1\problem2.py -----

# ----- Start of chapter1\problem3.py -----
import os

# Select the directory whose content you want to list 
directory_path = '/Games'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)
# ----- End of chapter1\problem3.py -----

# ----- Start of chapter2\datatype.py -----
a=1    #a is a integer
b=5.22  #b is a floating point number
c="abdul"  #c is a string
d=True    #d is aboolean 
e=None   #e is a none 

# ----- End of chapter2\datatype.py -----

# ----- Start of chapter2\input.py -----
a=input("Enter a number1: ")
b=input("Enter a number2: ")

print("Number a is:", a)
print("Number b is:", b)
print("Sum of a and b is:", int(a) / int(b))
# ----- End of chapter2\input.py -----

# ----- Start of chapter2\operators.py -----
#        # Arithmetic operatoors

# a=34
# b=4
# c=a+b
# print(c)

#         # assigment operator
# a=4-2 # assign 4-2 in a
# print(a)
# # b=6 #increment the value of b
# b=6 #decrement the value of b
# b-=3
# print(b)

# #         comparesion oprators 
# # ....this operators only give true or false
# d=5<4 #you use <,>,<=,>=,!=,==
# print(d)

            # logical opertaors
    # OR operator
# print("true or False is", True or False) 
# print("true or True is",True or True)  
# print("False or true is", False or True)  
# print("False or False is",  False or False) 
#     # AND operator
# print("true and False is", True and False) 
# print("true and True is",True and True)   
# print("False and true is", False and True)  
# print("False and False is",  False and False) 

# #         # not operator

# print("not True is", not True) 
# print("not False is", not False)
# ----- End of chapter2\operators.py -----

# ----- Start of chapter2\practiceset.py -----
a=1
b=2
print(a+b)
# ----- End of chapter2\practiceset.py -----

# ----- Start of chapter2\practiceset2.py -----
a=34
b=5
print("Reminder when a is divided by b is",a%b)
# ----- End of chapter2\practiceset2.py -----

# ----- Start of chapter2\practiceset3.py -----
a=input("enter the value of a: ")
print(type(a))
# ----- End of chapter2\practiceset3.py -----

# ----- Start of chapter2\problemset4.py -----
a=int (input("enter the value of a: "))
b=int(input("enter the value of b: "))
print(a>b)

# ----- End of chapter2\problemset4.py -----

# ----- Start of chapter2\problemset5.py -----
a=int (input("enter the value of a: "))
b=int(input("enter the value of b: "))



print("the average of these two number is ",(a+b)/2)


# ----- End of chapter2\problemset5.py -----

# ----- Start of chapter2\problemset6.py -----
a=int (input("enter your number: "))



print("the square of these two number is ", a**2)


# ----- End of chapter2\problemset6.py -----

# ----- Start of chapter2\type.py -----
a=31
t=type(a)#class 'int'>
print(t)

b=3.14
t=type(b)#class 'float'>
print(t)

c="hello"
t=type(c)#class 'str'>
print(t)
# ----- End of chapter2\type.py -----

# ----- Start of chapter2\variables.py -----
a=1  # a is a variable
b=2  # 1 and 2 are integers  
print(a+b)
# ----- End of chapter2\variables.py -----

# ----- Start of chapter3\01_problem.py -----
name=input("Enter your name: ")

print(f"Good afternoon,{name}")
# ----- End of chapter3\01_problem.py -----

# ----- Start of chapter3\02_problem.py -----
letter='''
Dear <|name|>,
    you are selected!
    <|date|>'''

print(letter.replace("<|name|>", "mohiz").replace("<|date|>", "07/09/2050"))
# ----- End of chapter3\02_problem.py -----

# ----- Start of chapter3\03_problem.py -----
name="Moiz is a good  boy  and  " 
print(name.find("good "))

# ----- End of chapter3\03_problem.py -----

# ----- Start of chapter3\04_problem.py -----
name="Moiz is a good boy" 
print(name.replace(" ", "="))
print(name)

# ----- End of chapter3\04_problem.py -----

# ----- Start of chapter3\05_problem.py -----
letter="dear moiz,\n\t you are selected on 07/09/2050.\nthanks"
print(letter)
# ----- End of chapter3\05_problem.py -----

# ----- Start of chapter3\escape_seq.py -----
    # escape_seq.py
         #\n is used to create a new line
       
a="moiz is a good boy\n  but not a bad boy"
print(a)

            #\t is used to create a tab space
b="moiz is a good boy\tbut not a bad"
print(b)

            #\\ is used to print a backslash
c="moiz is a good boy\\but not a bad"
print(c)
            #\' is used to print a single quote
d='moiz is a good boy\'but not a bad'
print(d)
            #\" is used to print a double quote
e="moiz is a good boy\"but not a bad"
print(e)    




# ----- End of chapter3\escape_seq.py -----

# ----- Start of chapter3\negative_slicing.py -----
name="abdul"
print(name[0:3]) 
print(name[-4:-1])
print(name[1:4 ])
print(name[:4])
print(name[1:])
# ----- End of chapter3\negative_slicing.py -----

# ----- Start of chapter3\strings.py -----
name="moheed"

shortname=name[0:4 ]

print(shortname)
# ----- End of chapter3\strings.py -----

# ----- Start of chapter3\str_function.py -----
name="mohiz"
print(len(name))
print(name.endswith("iz"))
print(name.startswith("mo"))
print(name.capitalize())
# ----- End of chapter3\str_function.py -----

# ----- Start of chapter4\list.py -----
friends=["apple", "banana", "cherry",5,35,45,True,False,"mohiz","ahsan"]
print(friends[0]) 
friends[0] = "orange" #list is mutable
print(friends[0])
# ----- End of chapter4\list.py -----

# ----- Start of chapter4\list_methods.py -----
friends=["apple", "banana", "cherry",5,35,45,True,False,"mohiz","ahsan"]
print(friends) 
friends.append("kiwi")  # Adding a new item to the list
print(friends)

l1 = [1, 2, 3]
l1.sort()  # Sorting the list in ascending order
print(l1)

l1.reverse()  # Reversing the order of the list
print(l1)

l1.insert(1, 4)  # Inserting an item at a specific index
print(l1)

l1.pop(l1.pop(3))  # Removing the last item from the list 
print(l1)

l1.remove(2)  # Removing a specific item from the list
print(l1)


# ----- End of chapter4\list_methods.py -----

# ----- Start of chapter4\tuples.py -----
a=(1,234,43545,252,False,"rohan")
print(a)
print(type(a))  # Output: <class 'tuple'>  
# ----- End of chapter4\tuples.py -----

# ----- Start of chapter4\tuples_method.py -----
a=(1,234,43545,252,False,"rohan")
print(a)
 
no=a.count(252)  # Count occurrences of 252 in the tuple
print(no)  # Check if 252 is in the tuple

i=a.index(252)  # Find the index of 252 in the tuple
print(i)  # Output the index of 252
# ----- End of chapter4\tuples_method.py -----
