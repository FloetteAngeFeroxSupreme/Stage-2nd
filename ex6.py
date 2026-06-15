def calculatrice(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b==0:
            return "impossible" # Or raise ValueError("Division by zero")
        else:
            return a/b
    else:
        return "opérateur invalide" # Or raise ValueError("Invalid operator")

if __name__ == "__main__":
    num1 = int(input("entrez un nombre: "))
    num2 = int(input("entrez un nombre: "))
    operator = input("entrez un opérateur: ")
    result = calculatrice(num1, num2, operator)
    print(result)