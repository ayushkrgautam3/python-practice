# Create a tuple storing first n terms of Fibonacci series
fibonacci = [0, 1]
a=int(input("Enter how many terms of fibonacci series:"))
for i in range(2, a):
    nt = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(nt)
ft = tuple(fibonacci)
print(a,"terms of Fibonacci series:")
print(ft)
