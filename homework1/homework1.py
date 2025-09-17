# File: homework1. py
# --- Variables and Data Types ---

a=10
b=1.5
c=3j
d= ("hello")
e=[1,2,3]
f = {"name": "lauren", "favorite fruit": "peaches"}
g=(1,2)
h=["apple", "banana", "strawberry"]
i=True
j=None
k=[True, "blue", 12]
l=str(14)
m=1e4

print(a)
print(type(a)) # a is an integer

print(b)
print(type(b)) # b is a float

print(c)
print(type(c)) # c is complex

print(d)
print(type(d)) # d is a string

print(e)
print(type(e)) # e is a list

print(f)
print(type(f)) # f is a dict or map

print(g)
print(type(g)) # g is a tuple

print(h)
print(type(h)) # h is a list

print(i)
print(type(i)) # i is a boolean

print(j)
print(type(j)) # j is a NoneType

print(k)
print(type(k)) # k is a list

print(l)
print(type(l)) # l is a string

print(m)
print(type(m)) # m is a float

# 1. I found 9 differnt types of data types
# 2. Integer, Float, Complex, String, List, Dict, Tuple, Boolean, NoneType
# m and b are both floats, d and l are both strings, and e h and k are all lists
# The data type of l was a string because the str() makes the input a string. This is also why l is not an integer
# Another data type is a range. (Ref: variable n)

n = range(5)
print (type(n))

# --- Booleans ---
print (10>9) # true, 10 is greater than 9
print (10==9) # false, 10 is not 9
print (10 <= 9) # false, 9 is not less than or equal than 10
print (bool("abc")) # true, abc is not empty
print (bool(123)) # true, 123 is not empty
print (bool(["apple", "cherry", "banana"])) # true, the list is not empty
print (bool(True)) # true
print (bool(False)) # false
print (bool(0)) # false
print (bool("")) # false
print (bool(" ")) # true
print (bool(())) # false 
print (bool(( ))) # false
print (bool([])) # false
print (bool({})) # false
print(bool(True and False)) # false because both not true
print(bool(True and True)) # true because both true
print(bool(False and False)) # false
print(bool(True or False)) # true
print(bool(True or True)) # true
print(bool(False or False)) # false
print(bool(not(False))) # true
print(bool(not(True))) # false

# I noticed that non empty values return true, and empty values return false. I also noticed that if the statements are correct they return true. and is only true if both are true, or is true if at least one is true, and not flips the result.
# What surprised me is that the space is still true because it counts is a non empty string

# 3 and 4 answered below
print (bool(99)) # true because not empty
print (bool(1>2)) # false because the statement isn't true


# --- Operators ---

# Arithmetic
print(10+5) # 15, the plus sign does addition wow so cool i never knew that
print(10-5) # 5, subtraction
print(2*4) # 8, multiplication
print(6/3) # 2. divides
print(5/2) # 2.5, divides
print(3**2) # 9, squares
print(15//2) # 7, divides then rounds down

# Comparison
print(5 == 2) # false, not equal
print(10 != 10) # false, because ! means not equal to
print(2 < 5 ) # true, inequality
print(12 > 5) # true, inequality
print(5 <= 6) # true. or inequality
print(1 >=10 ) # false

# Assignments
z = 5          # start with z = 5

z += 5         # same as z = z + 5 → 5 + 5 = 10
print(z)       # prints 10

z -= 4         # same as z = z - 4 → 10 - 4 = 6
print(z)       # prints 6

z *= 3         # same as z = z * 3 → 6 * 3 = 18
print(z)       # prints 18

# Logical 
# and -> combines both inputs and both must be true to result in true
print(5 > 2 and 10 > 3)   # true, because both comparisons are true
print(5 > 2 and 10 < 3)   # false, because the second comparison is false
# or -> either or input can be true for the result to be true
print(5 > 2 or 10 < 3)    # true, because the first comparison is true
print(5 < 2 or 10 < 3)    # false, because both comparisons are false
# not -> flips the boolean value, makes true into false, false into true
print(not(5 > 2))         # false, because 5 > 2 is true, and not flips it
print(not(5 < 2))         #true, because 5 < 2 is false, and not flips it

# More Questions
# / just divides, // rounds down to the nearest whole integer
# % gives the remainder after division, // rounds down to nearest whole integer
# you would use % to calculate the remainder:
print (5%2) #returns 1 as the remainder
# assignment operators go in order of the commands, like a+=b would be a plus b = a

# Strings
my_string="hello"
print(my_string) # Prints: hello
print(my_string[0]) # prints h, first letter
print(my_string[1]) # prints e, second letter
print(my_string[2]) # prints l. third
print(my_string[3]) # prints l, fourth
print(my_string[4]) # prints o, fifth
print(my_string[-1]) # prints o, last
print(my_string[1:3]) # prints 2nd and 4th, el
print(my_string[0:5:2]) # prints the start:stop:step
print(len(my_string)) # prints 5, number of characters
print(my_string+"goodbye") # prints hellogoodbye
print(my_string*7) # prints hello 7 times

# 3.4.1 questions
# slicing is a way to extract part of the sequence, like the 0:5:2
# result of 2. is hello my name is oski
# result f 3. is als hello my name is oski, exact same as before
# for f string there is a variable inside the string {}, thers no extra spaces, and it can evaluate any python expression inside

# 3.5 terminal commands
# cd - changes directories. use to move from one folder to another
# ls - lists the files and folders in the current directory
# ls -a - lists all files, including hidden files
# mkdir - creates a new directory (folder) in the current location
# cat - displays the contents of a file without like running the script
# pwd - prints current working directory
# cd .. - moves up one directory (to the parent folder)
# cd . - refers to the current directory
# cd ~ - moves to the home directory of the current user
# cp - copies files or directories
# mv - moves or renames files or directories
# rm - removes (deletes) files. be careful, cannot undo
# clear - clears the terminal screen
# grep - searches for text patterns inside files or output it doesnt work in windows

# three other commands not present: echo - prints text or variables to the terminal. use it like: echo "hello world", touch - creates a new empty file. use it like: touch newfile.txt, rmdir - removes an empty directory. use it like: rmdir foldername

# difference between ls and ls -a: -a lists all fires and directories even ones that start w/ .

# what is a hidden file: a hidden file is a file whose name starts with a (.). isnt shown by default

# three other flags: -l, -h, -r for ls. respectively: shows info about files, makes file sizes readable, and reverses order of output