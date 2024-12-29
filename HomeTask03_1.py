import match

print("****** Power Calculator ******")

number_first = float(input("Enter the firs number: "))
number_second = float(input("Enter the second number: "))
action_numbers = input("Enter the operation on numbers (+, -, *, /): ")
result = None

match action_numbers:
    case "+":
        result = number_first + number_second
    case "-":
        result = number_first - number_second
    case "*":
        result = number_first * number_second
    case "/" if number_second != 0:
        result = number_first / number_second
    case "/" if number_second == 0:
        result = "You can't divide by zero."
    case _:
        result = "Something wrong."

print(f"Result: {number_first} {action_numbers} {number_second} = {result}")

