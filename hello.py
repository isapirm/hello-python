# created by isapirm
print("hello world")

def sum(a, b):
    """
    Calculate the sum of two numbers
    """
    return a + b

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

total = sum(num1, num2)

print(f"The sum of {num1} and {num2} = {total}")