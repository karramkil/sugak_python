import math

def calculate_expression(x, y, a, b, formula):
    return eval(formula)

def main():

    x = 1.825
    y = 18.225
    formula = "abs(x**y/x - (y/x)**(1/3))"
    result = calculate_expression(x, y, 0, 0, formula)
    print("Вариант 1: x =", x, "y =", y)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

    a = -0.5
    b = 1.7
    t = 0.44
    formula = "b*math.sin(a*t**2*math.cos(2*t)) - 1"
    result = calculate_expression(0, 0, a, b, t, formula)
    print("\nВариант 2: a =", a, "b =", b, "t =", t)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

 
    x = -2.9
    a = 1.5
    b = 15.5
    formula = "(math.sqrt(x**2 + b) - b**2 * math.sin((x + a)/x)**3)"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 3: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
   print("Целая часть результата:", int(result))

 
   formula = "math.cos(x**3)**2 - x/(math.sqrt(a**2 + b**2))"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 4: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

    x = 0.5
    a = 0.7
    b = 0.05
    formula = "x**2*(x + 1)/b - math.sin((x + a))**2"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 5: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

    formula = "(math.sqrt(x*b/a) + math.cos((x + b)**3)**2)"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 6: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

    x = 0.2
    a = 1.1
    b = 0.004
    formula = "math.sin((x**2 + a)**2)**3 - (math.sqrt(x)/b)"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 7: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

    x = 0.61
    a = 0.3
    b = 0.9
    formula = "(a**2*x + b**(-x)*math.cos(a + b)*x)/(x + 1)"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 8: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

  
    formula = "(math.sqrt(x**2 + b) - b**2 * math.sin((x + a)/x)**3)"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 9: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))


    formula = "math.cos(x**3)**2 - x/(math.sqrt(a**2 + b**2))"
    result = calculate_expression(x, 0, a, b, formula)
    print("\nВариант 10: x =", x, "a =", a, "b =", b)
    print("Результат:", result)
    print("Целая часть результата:", int(result))

if __name__ == "__main__":
    main()
