
# One of the first projects anyone does is a simple calculator that takes in 2 numbers. 
# So I did that, but instead of taking each input in 3 different lines, I did it in one line. 

def add(num1 : int, num2 : int):

    return num1 + num2 

def subtract(num1 : int, num2 : int):

    return num1 - num2 

def multiply(num1 : int, num2 : int):

    return num1 * num2 

def divide(num1 : int, num2 : int):

    return num1 / num2


def main():
    
    print("Enter your equation in this format:")
    print("<number 1> <operation> <number 2>")

    equation = input().split()

    try:
        num1 = int(equation[0])
        operation = equation[1]
        num2 = int(equation[2]) 
    except ValueError: 
        print("\n")
        main() 
    except IndexError:
        print("Please follow the format!")
        main()
 
    result = {
        "+" : add, 
        "-" : subtract,
        "*" : multiply,
        "/" : divide 
    }.get(operation)(num1, num2) 

    print(result)

    print("\n")
    main() 

if __name__ == "__main__":
    main()