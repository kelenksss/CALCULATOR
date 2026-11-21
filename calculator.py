num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = int(input('''
select an operation
1 ------ +
2 ------ -
3 ------ *
4 ------ /
'''))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(num1 / num2)
else:
    print("Error")