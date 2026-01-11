#To check given number is prime or not
a=int(input("Enter a number:"))
b=int(a/2)+1
for i in range(2,b):
    r=a%i
    if r==0:
        print(a," is not a prime number.")
        break
else:
    print(a," is a prime number.")
