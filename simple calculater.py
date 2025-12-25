while True:
    print("Options: +  -  *  //  or q to quit")
    choice = input("Enter operation: ")
    if choice == 'q':
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == '+':
        print("Result:", a+b)
    if choice == '-':
        print("Result:", a-b)
    if choice == '*':
        print("Result:", a*b)
    if choice == '//':
        print("Result:", a//b)  # floor division (integer)