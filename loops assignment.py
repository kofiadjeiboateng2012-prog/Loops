number=int(input("Enter a number  you want to find the square of: "))
exponent=int(input("Enter the exponent you want to raise the number to: "))
result=1
for i in range(exponent):
    result=result*number

print("The result of", number, "raised to the power of", exponent, "is", result)
