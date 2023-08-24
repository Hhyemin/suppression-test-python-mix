def add(a, b):
    result = a + b  
    return result

def subtraction(a, b):
    result = a - b  
    return result

def main(operation):
    # pylint: disable=unused-argument
    x = "3" # type: ignore
    y = 5
    if operation == "add":
        print(add(x, y)) 
    elif operation == "subtraction":
        print(subtraction(x, y)) 

if __name__ == "__main__":
    operation = "add"
    main(operation)
