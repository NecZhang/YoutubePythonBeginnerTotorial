
try:
    n = 1 / 0
    number = int(input("Enter a number:"))
    print(number)

except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")