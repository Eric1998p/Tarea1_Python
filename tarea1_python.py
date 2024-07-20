#https://www.python.org/

#Podemos hacer comentarios de una línea utilizando el símbolo #

#Aunque también podemos comentar
#varias líneas utilizando múltiples
#símbolos #, uno al inicio de cada línea

"""
Otra forma que tenemos para hacer comentarios
de varias líneas es utilizando tres dobles 
comillas; 3 al inicio y otras 3 al final 
"""

"""
En Python, la distinción entre variables y constantes no es tan 
estricta como en algunos otros lenguajes de programación. Python 
no tiene palabras clave especiales para declarar constantes, pero 
se pueden seguir ciertas convenciones para indicar que una variable 
debe tratarse como una constante.

En Python, la distinción entre variables y constantes no es tan 
estricta como en algunos otros lenguajes de programación. Python no 
tiene palabras clave especiales para declarar constantes, pero se 
pueden seguir ciertas convenciones para indicar que una variable debe 
tratarse como una constante. Aquí tienes una explicación detallada

Para las constantes, la convención es escribir sus nombres en mayúsculas, 
para indicar que su valor no debería cambiar.

Las variables en Python se pueden declarar simplemente asignando un valor 
a un nombre de variable. No se necesita una palabra clave especial para 
declarar una variable.

"""

#Ejemplo de variable

coche = "eléctrico"
boool1 = True
number1 = 5.2

print(coche, boool1, number1)

#Ejemplo de constante

#Importaré una biblioteca para mandar a llamar a la constante pi
import numpy as np

PI = np.pi
E = np.e
CONST = 2

print(PI, E, CONST)

"""

Los tipos de datos primitivos son los más básicos que un lenguaje de 
programación proporciona sin necesidad de importar módulos adicionales. 
Estos tipos de datos son la base para la construcción y manipulación de 
datos más complejos. Estos pueden ser: enteros, flotantes, complejos, 
cadenas de caracteres, booleanos, NoneType, bytes, bytearray y memoryview.

"""
#Los datos de tipo entero (int) son números enteros, es decir: -5, 0, 10, etc

int1 = 25
print(int1,type(int1))

#Los datos de tipo flotantes (float) son números reales o de punto flotante,
#por ejemplo: 3.1416, 2.7182, 1.6180, 0.0, -3.33

float1 = 25.2
print(float1, type(float1))

#Los datos de tipo complejos (complex) son números complejos, por ejemplo:
#3+5j, 7.25-np.pi*1j, 7+0j, etc

complex1 = 3+np.pi*1j
print(complex1, type(complex1))

#Los datos de tipo cadena de caracteres o string (str) son secuencias de 
#caracteres, por ejemplo: "Hola", "Python", "123", etc

str1 = "Hola, hoy es un buen día. Hoy es 17 de julio"
print(str1, type(str1))

#Los datos de tipo booleano (bool) son valores que solo pueden ser True o 
#False, esto se utiliza para representar verdadero y falso.

bool1 = True
print(bool1, type(bool1))

#Los datos de tipo NoneType (None) son un tipo especial que representan la
#la ausencia de un valor.

none1 = None
print(none1, type(none1))

#Los datos de tipo bytes (bytes) son secuencias de valores de bytes inmutables,
#pueden ser utilizados para representar datos binarios como imágenes, archivos, etc.
#Un byte es una unidad de almacenamiento de datos que equivale a 8 bits. Los 
#bytes son la unidad básica de información utilizada en la mayoría de las 
#arquitecturas de computadoras modernas y en sistemas de comunicación digital. 
#Un byte tiene 8 bits. Dado que cada bit puede tener un valor de 0 o 1, un byte 
#puede representar 256 valores diferentes (de 0 a 255)

bin1 = b'Hola, mundo!'
print(bin1, type(bin1))

#Los datos de tipo bytearray (bytearray) son secuencias de bytes mutables.

bytearray1 = bytearray([65, 66, 100])
bytearray2 = bytearray("¡Hola, mundo!", 'utf-8')
print(bytearray1, type(bytearray1))
print(bytearray2, type(bytearray2))

#Un memoryview permite acceder y manipular datos sin copiarlos, muy útil para 
#manejar grandes cantidades de datos o para trabajar con subconjuntos de datos 
#de manera eficiente.


# Crear un memoryview a partir del objeto bytes
memoryview1 = memoryview(bin1)
print(memoryview1, type(memoryview1))

print("¡Hola, Python!")

#Operadores aritméticos: se utilizan para realizar operaciones matemáticas
#básicas. Estas operaciones son

#Suma +

x = 5
y = 10
sum = x + y
print("Suma: {}".format(sum))

#Resta -

x = 5
y = 10
substraction = x - y
print("Resta: {}".format(substraction))

#Multiplicación *

x = 5
y = 10
multiplication = x * y
print("Multiplicación: {}".format(multiplication))

#División /

x = 5
y = 10
division = x / y
print("División: {}".format(division))

#Exponenciación y raiz ** (la raiz es elevar un número a una potencia fraccionaria)

x = 4
y = 2
exponent = x ** y

raiz = x**(1/y)
print("Exponenciación: {}".format(exponent))
print("Raiz: {}".format(raiz))

#Módulo % (nos devuelve el residuo de la división de dos números)

x = 5
y = 10
modulo = x % y
print("Módulo: {}".format(modulo))

#División entera // (consiste en dividir un número entero entre otro
#y obtener el cociente entero, descartando el residuo)

x = 15
y = 10
division_entera = x // y
print("División Entera: {}".format(division_entera))

#Operadores de asignación: asignan valores a las variables

#Asignación = 

x = 5
print(x)

#Asignación de adición +=
#Es equivalente a x = x + 5

x = 5
x += 5
print(x)

#Asignación de sustracción -=
#Es equivalente a x = x - 5

x = 5
x -= 5
print(x)

#Asignación de multiplicación *=
#Es equivalente a x = x * 5
x = 5
x *= 5
print(x)

#Asignación de división /=
#Es equivalente a x = x / 5

x = 5
x /= 5
print(x)

#Asignación de exponenciación (y raiz) **=
#Es equivalente a x = x **2


x = 4
x **= 2
print(x)

#Asignación de módulo %=
#Es equivalente a x = x % 5

x = 5
x %= 5
print(x)

#Asignación de división entera //=
#Es equivalente a x = x // 10

x = 15
x //= 10
print(x)

#Los operadores de asignación de AND bit a bit &= combinan una 
#operación bit a bit con una asignación en una sola expresión. Estos operadores 
#permiten modificar el valor de una variable aplicando una operación bit a bit 
#con otro valor y luego asignar el resultado de vuelta a la misma variable
#5 en binario es 101 y 3 en binario es 011, por lo que al aplicar & obtenemos
#001 ya que es 1 en ambos solo en el primer dígito. Como 001 es equivalente a 1,
#entonces 1 es el resultado.
#Es equivalente a x = x & 3

x = 5
x &= 3
print(x)

#Operadores de asignación de OR bit a bit |=
#Es equivalente a x = x | 4

x = 5
x |= 4
print(x)

#Operadores de asignación de XOR bit a bit ^=
#Es equivalente a x = x ^ 3

x = 5
x ^= 4
print(x)

#Asignación de desplazamiento a la izquierda <<=
#Es equivalente a x = x << 3
#El operador de desplazamiento a la izquierda mueve los bits de un número 
#hacia la izquierda por un número específico de posiciones. Los bits 
#desplazados hacia la izquierda se llenan con ceros.

x = 5
x <<= 1
print(x)

#Asignación de desplazamiento a la derecha
#Es equivalente a x = x >> 3

x = 5
x >>= 1
print(x)

#Operadores de comparación: se utilizan para comparar dos valores

#Igual a ==

x = 5
y = 5
print(x == y)

#No igual a != 

x = 5
y = 6
print(x!= y)

#Menor que <

x = 5
y = 10
print(x < y)

#Mayor que >

x = 10
y = 5
print(x > y)

#Menor o igual que <=

x = 5
y = 10
print(x <= y)

#Mayor o igual que >=

x = 10
y = 5
print(x >= y)

#Operadores lógicos and or not: se utilizan para combinar declaraciones
#condicionales. and devuelve True si ambas expresiones son verdaderas. or 
#devuelve True si al menos una expresión es verdadera. not invierte el valor
#de una expresión (si es False, entonces la invierte a True).

#Operador and

bool1 = True
bool2 = False
bool3 = True

print(bool1 and bool2, bool1 and bool3)

#Operador or

bool1 = True
bool2 = False
bool3 = False

print(bool1 or bool2, bool2 or bool3)

#Operador not

bool1 = True

print(not bool1)

#Operadores de identidad: se utiliza para comprobar si dos 
#referencias apuntan al mismo objeto en la memoria. En otras palabras, 
#verifica si las variables comparadas son exactamente el mismo objeto, no 
#solo si tienen el mismo valor (como en el caso de operadores de comparación).

#Operador is

x = [1, 2, 3]
y = [1, 2, 3]

print(x is y, x is x)

#Operador is not

x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y, x is not x)

#operadores de pertenencia: se utilizan para comprobar si una secuencia contiene 
#un valor específico

#Operador in

x = [1, 2, 3, 4, 5]
value = 3

print(value in x)

#Operador not in

x = [1, 2, 3, 4, 5]
value = 6

print(value not in x)

#Operadores AND bit a bit &

x = 5
y = 3

print(x & y)

#Operadores OR bit a bit |

x = 5
y = 3

print(x | y)

#Operadores XOR bit a bit ^

x = 5
y = 3

print(x ^ y)

#Operadores NOT bit a bit ~
#Este operador invierte todos los bits de un número. En otras palabras, 
#convierte todos los bits 1 en 0 y viceversa.vPython utiliza el complemento a 
#dos para representarvnúmeros negativos, por lo que el resultado de ~a es 
#-(a + 1)

x = 5

print(~x)

#Operadores de desplazamiento a la izquierda <<

x = 5

print(x << 1)

#Operadores de desplazamiento a la derecha >>

x = 5

print(x >> 1)

#Estructuras Condicionales
#Nos permiten ejecutar bloques de código basados en condiciones.

#if
#La sentencia if evalúa una condición. Si la condición es True, ejecuta el 
#bloque de código asociado.

#elif
#La sentencia elif (abreviatura de "else if") permite verificar múltiples 
#condiciones si la condición anterior (if o elif) es falsa. Puedes tener 
#múltiples elif después de una sentencia if.

#else
#La sentencia else se utiliza para ejecutar un bloque de código si ninguna de 
#las condiciones anteriores (if o elif) es verdadera. No toma una condición y 
#es opcional.

#Ejemplo de if, elif y else

x = float(input("Dame un número real: "))

if x > 15:
    print("x es mayor que 15")
elif x > 5:
    print("x es mayor que 5 pero menor o igual a 15")
else:
    print("x es menor o igual a 5")

#Otra forma de escribir if-else

x = 10
mensaje = "x es mayor que 5" if x > 5 else "x es menor o igual a 5"
print(mensaje)

#pass
#Es un marcador de posición que no hace nada, usado cuando se requiere una 
#sintaxis pero no se desea ejecutar ningún código.

if x > 0:
    pass  # Aquí no pasa nada

#Estructuras Iterativas
#Permiten ejecutar repetidamente un bloque de código.

#while
#Ejecuta un bloque de código mientras la condición sea verdadera. Ejemplo:

x = 0
while x < 5:
    print(x)
    x += 1

#for 
#Itera sobre una secuencia (como una lista, tupla, diccionario, conjunto o 
#cadena) y ejecuta un bloque de código.

#break
#Interrumpe la ejecución del bucle. Ejemplo:

for i in range(10):
    if i == 7:
        break
    print("valor " + str(i))

#continue
#Salta a la siguiente iteración del bucle. Ejemplo:

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#else (con bucles)

for i in range(5):
    print(i)
else:
    print("Bucle terminado normalmente")

#Estructuras de Manejo de Excepciones
#permiten manejar errores y excepciones que pueden ocurrir durante la 
#ejecución de un programa, permitiendo que el programa continúe su 
#ejecución en lugar de detenerse cuando ocurre un error.

#try-except-else

try:
    # Código que puede generar una excepción
    resultado = 10 / 0
    #Nombre de la excepción
except ZeroDivisionError:
    # Código para manejar la excepción
    print("No se puede dividir por cero")
    #El bloque else se ejecuta si no ocurre ninguna excepción.
else:
    print("La división fue exitosa")

#try-except-finally
#El bloque finally se ejecuta siempre, haya o no excepción.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esta línea siempre se ejecuta")

#raise

if x < 0:
    raise ValueError("El valor no puede ser negativo")

#assert
#Prueba si una condición es verdadera, y si no, lanza una excepción 
#AssertionError

assert x > 0, "x debe ser positivo"

#Otra Estructura de Control

#with
#Gestiona contextos de recursos, asegurando que se cierren correctamente
#después de su uso. Esto es crucial en situaciones donde se deben manejar 
#recursos que requieren apertura y cierre explícitos, como archivos, 
#conexiones a bases de datos, y otros recursos que deben ser liberados después
#de su uso para evitar pérdidas de memoria o bloqueos de recursos.

with open("with.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


#Ahora, crearé un programa que imprima todos lo números del 10 al 100, excepto
#el 66 ni múltiplos de 3

for i in range(0,100+1):
    #Está de más poner la condición del 66, puesto que es múltiplo de 3,
    #pero aún así la pondré.
    if i == 66 or i % 3 == 0:
        continue
    print(i)





#Como adicional, voy a poner estructuras de datos como list, tuplas, diccionarios
#conjuntos, range, etc.
#-ya después agrego ejemplos de bytes con imágenes y así

###Al final revisar de nuevo las instrucciones.

