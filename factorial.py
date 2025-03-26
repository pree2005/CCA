def facto(int x):
  if x==1:
    return 1
  else:
    return facto(n-1)*n
a=int(input("Enter the number: "))
b=facto(a)
print("Factorial of a: ",b)
