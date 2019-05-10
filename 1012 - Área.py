A, B, C = map(float, input().split())
pi = 3.14159

triangulo = (A*C) /2
circulo = 3.14159*(C**2)
trapezio = ((A+B)*C) / 2
quadrado = B*B
retangulo = A*B


print("TRIANGULO: %.3f" %triangulo)
print("CIRCULO: %.3f" %circulo)
print("TRAPEZIO: %.3f" %trapezio)
print("QUADRADO: %.3f" %quadrado)
print("RETANGULO: %.3f" %retangulo)
