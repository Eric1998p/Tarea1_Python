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



"""

memoryview: Permite acceder a los datos internos de un objeto bytes sin copiarlos.
python
Copiar código
mv = memoryview(b'Hola')
"""




#Como adicional, voy a poner estructuras de datos como list, tuplas, diccionarios
#conjuntos, range, etc.