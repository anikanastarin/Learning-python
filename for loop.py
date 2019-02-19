'''#1. Print all the even number from 1 to 50.

for x in range(2, 51, 2):
    print(x)
    
#2. Take an integer input from the user, and use that integer to make a table as output.

a = [int(x) for x in input().split()]
titles = [a]
data = [titles] + list(zip(a))

for i, d in enumerate(data):
    line = '|'.join(str(x).ljust(12) for x in d)
    print(line)
    if i == 0:
        print('-' * len(line))
#3. Make multiplication tables for 1 to 20.

for x in range (1,21,1):
    print("\n namta",x,"\n")
    for y in range (1,11,1):
        print(x,"X",y,"=",x*y)
#4. Write a program to find factorial of an input.

N = int(input("Input factorial you want to calculate: "))
ans = 1
for i in range(1,N+1):
    ans = ans*i
print(ans)'''

'''#5. Take an integer as input and show if it’s prime or not.

Input = int(input("Enter a number:"))

if Input > 1:
   
   for i in range(2,Input):
       if (Input % i) == 0:
           print(Input,"is not a prime number")
           break
   else:
       print(Input,"is a prime number")
       
else:
   print(Input,"is not a prime number")'''

