def fact(n):
  if n<=1:
    return 1
  else:
    return n*fact(n-1)
m=int(input("Enter the value:"))
print("The Factorial of m:", fact(m))