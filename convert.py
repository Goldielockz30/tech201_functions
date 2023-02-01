def convert(num1, num2: float = 100) -> float:
    return num1 / num2
num1 = int(input("Enter the number of centemetres you would like to convert to metres: "))
num2 = 100
print("Your converted value is")
print(convert(num1, num2))

def convert(num1, num2: float = 100) -> float:
    return num1 * num2
num1 = int(input("Enter the number of metres you would like to convert to feet: "))
num2 = 3.280839895
print("Your converted value is")
print(convert(num1, num2))