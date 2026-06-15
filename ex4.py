def triangle(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return "invalide"
    elif a+b<=c or a+c<=b or b+c<=a:
        return "invalide"
    elif a==b==c:
        return "equilateral"
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        return "rectangle"
        if a==b or b==c or a==c:
            return "isosceles"
    elif a==b or b==c or a==c:
        return "isosceles"
    else:
        return "quelconque"
