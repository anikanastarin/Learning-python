'''#1. Write a function to print out numbers in a range.Input = my_range(2, 6)Output = 2, 3, 4, 5, 6
def my_range(a,b):
    for c in range(a,b+1):
        print (c)
my_range(2,6)

#2. Now make a default parameter for “difference” in the previous function and set it to 1. When the difference value is passed, the difference between the numbers should change accordingly.
def increment(a,b,diff=1):
    w=a;
    while w<=b:
        print(w)
        w=w+diff
        
increment(2,6)
#3. Write a Python program to reverse a string. Go to the editor Sample String: "1234abcd" Expected Output: "dcba4321"
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
s = "123abcd" 
print ("Sample String: ",end="") 
print (s) 
print ("Reverse Output: ",end="") 
print (reverse(s))

#4. Write a function to return the factorial of an input. Assign the value to a new variable and print it.
def factorial(x):
    a=1;
    for c in range (0,x):
        a=a*(x-c)
    
    return a
z=int(input("Input Number:"))
factorial(z)
w=factorial(z)
print("value of new variable:",w)
#5. Write a Python function that takes a number as a parameter and check the number is prime or not. Return True or False.

def prime(y):
    f=0;
    for x in range(2,y):
        if y%x==0:
            f=f+1
            if f>=1:
                return False
            
            else:
                return True
c=int(input("Enter any  prime integer:"))
print(prime(c))'''


