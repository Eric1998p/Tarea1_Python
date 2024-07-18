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

#Los datos de tipo bytes (bytes) son secuencias de valores de bytes,
#pueden ser utilizados para representar datos binarios como imágenes, archivos, etc.









"""
Numéricos
Enteros (int): Representan números enteros, tanto positivos como negativos, sin parte decimal.
python
Copiar código
x = 10
y = -5
Flotantes (float): Representan números con parte decimal.
python
Copiar código
pi = 3.14159
e = 2.718
Números complejos (complex): Representan números complejos en la forma a + bj, donde a es la parte real y b es la parte imaginaria.
python
Copiar código
z = 2 + 3j
Tipos de Datos de Secuencia
Cadenas de caracteres (str): Secuencias de caracteres, tanto letras como dígitos y otros símbolos.
python
Copiar código
nombre = "Juan"
saludo = 'Hola'
Tipos de Datos Booleanos
Booleanos (bool): Representan valores de verdad, pueden ser True o False.
python
Copiar código
es_mayor = True
es_menor = False
Tipo de Datos Especial
NoneType: Representa la ausencia de un valor.
python
Copiar código
valor_nulo = None
Tipos de Datos Binarios
bytes: Secuencia de enteros en el rango de 0 a 255.
python
Copiar código
b = b'Hola'
bytearray: Similar a bytes, pero mutable.
python
Copiar código
ba = bytearray([65, 66, 67])
memoryview: Permite acceder a los datos internos de un objeto bytes sin copiarlos.
python
Copiar código
mv = memoryview(b'Hola')
Resumen de los Tipos de Datos Primitivos en Python
int: Enteros, como 10 o -5.
float: Números de punto flotante, como 3.14159 o 2.718.
complex: Números complejos, como 2 + 3j.
str: Cadenas de caracteres, como "Hola" o 'Mundo'.
bool: Valores booleanos, True o False.
NoneType: El tipo del valor None, que representa la ausencia de un valor.
bytes: Secuencias inmutables de enteros en el rango de 0 a 255.
bytearray: Secuencias mutables de enteros en el rango de 0 a 255.
memoryview: Permite el acceso a los datos del buffer subyacente sin copiarlos.
"""




#Como adicional, voy a poner estructuras de datos como list, tuplas, diccionarios
#conjuntos, range, etc.