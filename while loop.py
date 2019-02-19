'''#1. Print all the even number from 1 to 50.

a=1
while a<=50:
    if a%2==0:
        print(a)
    a=a+1


#2. Take an integer input from the user, and use that integer to make a table as output.





#3. Make multiplication tables for 1 to 20.

a=1
while a<=20:
    i=1
    print("\n namta",a,"\n")
    while i<=10:
        print(i,"X",a,"=",i*a)
        i=i+1
     
    a=a+1


#4. Write a program to find factorial of an input.

a = int(input("Enter a number: "))
def factorial (a):
    j = 1
    while a >= 1:
        j = j*a
        a=a-1
    return j
print ("The factorial of",a,"is",factorial(a))



#5. Take an integer as input and show if it’s prime or not.

i=2
num=int(input("enter number:"))
while i<=num:
    if (num%i)==0:
        print (num, "is not a prime number.")
        i = i + 1
    else:
        print (num, "is a prime number.")
        break'''


