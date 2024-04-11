try:
    answer = 10/0
    number = int(input("Ënter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")