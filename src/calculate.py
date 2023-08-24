def add(a, b):
    result = a + b  
    return result

def subtraction(a, b):
    result = a - b  
    return result

def main(operation):
    x = "10" # type: ignore
    y = 5
    if operation == "add":
        print(add(x, y)) 
    elif operation == "subtraction":
        print(subtraction(x, y)) 

if __name__ == "__main__":
    operation = "subtraction"
    main(operation)
