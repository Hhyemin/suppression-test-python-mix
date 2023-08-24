def add(a, b):
    result = a + b  
    return result

def main(operation):
    # pylint: disable=unused-argument
    x = 3
    y = 5
    print(add(x, y)) 

if __name__ == "__main__":
    operation = "add"
    main(operation)
