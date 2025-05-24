try: 
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    
    print("What Kind of Operation Wanted to perform.\nPress + for Addition \nPress - for Substration \nPress * for Multiplication \nPress / for Division")
    
    o = input("Enter Operation to Perform : ")

    match o:
        case "+":
            print(f"The Addition of {a} and {b} is {a + b}")
        case "-":
            print(f"The Substraction of {a} and {b} is {a - b}")
        case "*":
            print(f"The Multiplication of {a} and {b} is {a * b}")
        case "/":
            print(f"The Division of {a} and {b} is {a / b}")
            
except Exception as e:
    print("Enter a valid value of a and b")