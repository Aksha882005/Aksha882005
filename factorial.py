def Factorial(n):
    if n==0:
       return 1
    return(n*Factorial(n-1))
num=int(input("Enter a Number to find it's Factorial value"))
print("Factorial of", num," is:",Factorial(num))