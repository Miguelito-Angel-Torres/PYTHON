#La busqueda : Metodo(find); si se encuentra devuelve la posicion que se encuentra el caracter
# caso contrario devuelve -1
msj = "Hola Maria"
buscar_subcadena = msj.find("H");
print(buscar_subcadena);
#La extraccion: Se trata de sacar fuera de una cadena,una porcion de la misma segun su posicion dentro de ella.
extraer_subcadena = msj[1:3];
print(extraer_subcadena);
#Palabras reservadas( and del for is raise assert if  else if from lambda return 
# break global not try class expcept or while continue exec import yield def finally
# in print):
# break para salirse del while o for.
import time
boolwhile = True;
cont = 0
while(boolwhile):
    print("Contador va por el numero: " + str(cont))
    time.sleep(2);
    cont = cont + 1
    if(cont == 1): break
#Operador Aritmetica: // indica que no agregue decimales
print("Division entera: " + str(4//2));
# Saber que tipo de dato pertenece:
print(type(boolwhile))
# Entrada de datos:
#num = int(input("Ingrese numero: "));
# redondiar numero
nu1 = 7.777777
print(round(nu1, 2));
# Convertir cualquier cadena de caracter a minusculo.
convertir_letra = msj.lower()
print(convertir_letra)
# not : Operador que niega la condicion,palabra:"No es"
# parametro end evita el salto de linea de un print
print(msj, end=" Juanita ")
# parametro sep controla la separacion de los elementos que deseas imprimir
print(msj,"1",sep=",")
# While: x=1 while x < 2: print(x) x +=1
# Break y Continue 
contador = 0
#while contador < 10: contador += 1 if(contador == 5): break print("Valor actual de la variable",contador)
# while contador < 10: contador +=1  if(contador == 5): continue print("Valor actual de la variable",contador)
#len: Los espacios cuentan como caracter,cantidad = len("H H H H ") print(cantidad) 
# format() : concatena sin importar que sea String o Numerico.
#nombre,edad = "M",1
print("Hola {nombre} tiene {edad} ".format(nombre = "Z",edad = 15))
print("Hola {1}  tiene {0}".format("Z",15))
print("Hola {}  tiene {}".format("Z",15))
# Concatenacion f-Strings print(f"{5*2}")
# metodo strip(),rstrip() y lstrip()
# strip() solo puede eliminar los caracteres al inicio y final de la cadena, y no la parte central
# si no se le especifica caracteres a eliminar, solo eliminara espacios en blancos y saltos de linea
print("\tManito mas nada Lucas\n".strip())
print("\tHola Ernesto\n".strip("s tHo\t\n"))
# rstrip() Se utiliza para eliminar unicamente caracteres especificado al final de una cadena
#si no se le especifica caracteres a eliminar, solo eliminara espacios en blancos y saltos de linea
print("\tHola Ernesto\n".rstrip("s tHo\t\n"))
# lstrip() Se ultiza para eliminar unicamente caracteres especificado al inicio de una cadena
#si no se le especifica caracteres a eliminar, solo eliminara espacios en blancos y saltos de linea
print("\tHola Ernesto\n".lstrip("s tHo\t\n"))
# istitle() y title()
print("Maria Muquitas".istitle())
print("MARIA MUquitas".title())
# islower() lower(): Convierte la cadena de caracteres en miniscula
# isupper() y upper(): Convierte la cadena de caracteres en mayuscula
print("maria muquitas".islower())
print("MARIA MUQuitas".lower())
print("maria Muquitas".isupper())
print("Maria Muquotas".upper())
# swapcase() :  invertir todas las letras de una cadena de caracteres, donde las mayusculas
# se convierten en minusculas y las minusculas se convierten en mayusculas.
print("mMARIA mUQUITAS".swapcase())
# capitalize() : Devuelve que la primera letra debe estar en mayuscula y las demas letras en minusculas
print("Maria MUQuitas".capitalize())
# center() , ljust() y rjust()
print("Maria Muquitas".center(25,"="))
print("Maria Muquitas".ljust(25,"=")) # alinear el String a la izquierda
print("Maria Muquitas".rjust(25,"=")) # aliniar el String a la derecha
# count() Necesidad de conocer la cantidad de veces que aparece una cadena
# o caracter en especifico dentro de un texto
print(len("MariaLucas"))
print("Maria Lucas".count("a",3,10))
#  startswith() y endswith()
# startswith() : Se utiliza para comprobar si una cadena de caracteres comienza con una
# subcadena en particular.
print("Diana se peina sola".startswith("d"))
# endswith() : Se utiliza para comprobar si una cadena de caracteres termina con una subcadena
# en particular
print("Diana se peina sola".endswith("A"))
# Substrings :
print("Diana se peina sola"[1:4:1]);
# bucle for: Es una estructura de control que nos permite repetir un bloque de instrucciones,cierta
# cantidad de veces.
# objeto iterable: Es aquel que permite recorrer sus elementos uno a uno
string = "Ho"
for caracter in string:
    print(f"Caracter : {caracter}")
# bucle for y la clase range()
#for indice in range(1,5): print(indice)
# Lista : crea una coleccion de elementos ordenados: Lista_Homogenea = [1,2,3,4,5] Lista_heterogenea = ["M",1,True].
marcas = ["Apple","Sonic","LG","Samsung","Xiomi"]
#marcas[1] = "Huawai"
#marcas[-3] = "Desconocido"
# Cambio el valor de los elementos y agrego otro elemento.
#marcas[1:3] = ["Huawai","Desconocido","Chinazo"]
# Cambio el valor de los elementos y elimino el sgt elemento
#marcas[0:3] = "Japon","Chinaze"
#marcas[:] = "x"
print(marcas[1:3]) # Siempre nos va devolver en corchetes indicando el tipo de dato.
# Agregar elementos a una lista , siempre al final de la lista
#marcas.append("EE.UU")
# Insertar elementos a una lista , en una posicion determinada
marcas.insert(0,"Ruso")
# Eliminar elementos de una lista , sin parametro indica eliminar el ultimo elemento de la lista,tambien return el elemento que se elimino
eliminado = marcas.pop()
print(eliminado)  
# Eliminar elementos de una lista , especificamos como parametro el elemento que seamos eliminar.
# Supongamos que un mismo elemento varias veces , solo va eliminar el elemento que estamos indicando una sola vez.      
marcas.remove("Sonic")                                                                                                                                                                                            
print(marcas[:])
# Instruccion DEL: Elimina una lista, elimina una posicion de la lista o puede eliminar dos o mas elementos, 
animales = ["perro","gato","conejo"]
#del animales[0:2]
# del animales Elimina completamente la lista
# del animales[:] Indica elimina de inicio a fin todo los elementos pero no elimina el array
# Invertir una lista : modifica las posiciones de la lista actual,en lugar de crear una nueva lista
animales.reverse()
#print(animales)
# Ordenar los elementos de una lista : Tanto en orden ascendente o descendente, Si no hay argumento lo realiza en orden ascedente
animales.sort(reverse = True)
print(animales)
# Buscar elemento de una lista y devuelve la posicion del elemento.
print(animales.index("conejo",0,3))
# Concatenar listas: Unir dos o mas listas para formar una unica lista, objeto iterable array y range
juguetes = ["robot","mickey","mini"]
juguetes.extend(animales)
juguetes.extend(range(30,100,10))
print(juguetes)
# Sumar elementos de una lista, segundo parametro debe ir un valor inicial
num = [10,20,30]
print(sum(num,-10))
print(sum(range(30,100,10)))
# Constructor list() - Convertir objetos a listas, si esta vacia crea un lista vacia
devuelve = list(range(30,100,10))
devuelve1 = list("Ernesto")
print(devuelve1[::-1])
# Listas anidadas,son listas dentro de otra lista.
lista = [1,[1,2,3]]
print(lista[1][0])
# Matrices,son una estructura de datos bidimensional, cuyo elementos son 
# organizados  en filas y columnas , siempre es fila primero.
matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
print(matrix[2][1])
matrix.append([9,6,4])
for row in matrix:
    for element in row:
        print(element, end= "")
    print()
for row in range(0,len(matrix),1):
    print(matrix[row][0])
    print(matrix[row][1])
    print(matrix[row][2])
# Suma de matrices:
print()
matriznu1 = [
            [1,2,3],
            [4,5,6],
            [7,8,9] ]
matriznu2 = [
            [9,8,7],
            [6,5,4],
            [3,2,1] ]

nueva_fila = []
for fila in range(0,len(matriznu1),1):
    matriznu3 = []
    for columna in range(0,len(matriznu1[0])):
        matriznu3.append(matriznu1[fila][columna] + matriznu2[fila][columna])
    nueva_fila.append(matriznu3)
print(nueva_fila)
# Diccionario Python:
nombre_diccionario = {"a":1,"numbers":[1,2,3,4],"group":{"a":1,"b":2}}
print(nombre_diccionario["a"])
print(nombre_diccionario["numbers"][0])
print(nombre_diccionario["group"]["a"])
# El metodo items(),keys() y values() nos permiten acceder a diferentes partes del 
# diccionario y tabajar con ellas de manaera independiente
# items : devuelve todos los elementos del diccionario como una lista de tuplas.
print(list(nombre_diccionario.items()))
# keys devuelve una lista de todas las claves del diccionario
print(list(nombre_diccionario.keys()))
# values devuelve una lista de todas los valores del diccionario
print(list(nombre_diccionario.values()))
# metodo clear() : se utiliza para eliminar todos los elementos de un objetos
lista_eliminar = [1,2,3]
diccionario_eliminar = {"a":1,"b":2}
#lista_eliminar.clear()
#diccionario_eliminar.clear()
#print(lista_eliminar, diccionario_eliminar)
# Modificar y agregar elementos a un diccionario
diccionario_eliminar["a"] = "Modificado"
diccionario_eliminar["c"] = "Agregacion"
print(diccionario_eliminar)
# Metodo copy() Se utiliza para crear una copia de un objeto , puede ser lista,matrices o diccionarios
copialista = lista_eliminar.copy()
copiadicc = diccionario_eliminar.copy()
print(copialista , copiadicc)
# Metodo fromkeys() , dict : abreviatura de la palabra diccionario , si no hay valor coloca: None
# sequence es la secuencia de claves 
sequence1 = ["1","2","3"]
sequence2 = {1:"Obtener valor",2:"2",3:"3"}
sequence3 = "Numeros" 
name_dic = dict.fromkeys(sequence1,"numeros")
name_dic1 = dict.fromkeys(sequence2,"numeros")
name_dic2 = dict.fromkeys(sequence3,"numeros")
print(name_dic)
print(name_dic1,name_dic2)
# Get() se utiliza para obtener los valores que estan asociados a cada una de las claves
# de un diccionario,la clave del valor que deseas obtener.
print(sequence2.get(4,"No existe"))
#popitem
#print(list(sequence2.popitem()))
print(sequence2)
# tupla es constante es una lista de elementos, no se puede modificar
tupla = ("a","b","c","d","e","f","g","h","i")
print(tupla[2:5])
print(tuple(sequence1))
print(tuple(sequence2)) # Agarra las llaves para convertir en tuplas un diccionario
print(tuple(sequence3))
print("1" in sequence1)
for key,value in sequence2.items():
    print(f"{key}: {value}")
#print(sequence2.pop(1))
#del sequence2[1]
sequence2.update({"Agregacion" : 4})
print(sequence2)
# *args -Argumento arbitrarios : Son parametros de comodines que puedes colocar N cantidad de valores
def alumnos(*args):
    print(f"El ultimo alumnos es {args[5]} y el primero es {args[0]}")
alumnos("Miguel","Ana","Antonio",1,2,3)
def alumnos_prof(profesor,sustituto,*args):
    print(f"Prof: {profesor} Sus: {sustituto}")
    for x in args:
        print(f" Alumno: {x}")
lista_alumnos = ["Andres","Lucas"]
alumnos_prof("Lucas","Anita","Maria","Juanita","Mallqui")
# **kwatgs - Diccionarios arbitrarios
def colores(**kwargs):
    print("Color: " + kwargs["color1"])
colores(color1="roja",color2="azul",color3="verde")
# Clases y objetos, self hace referencia al objeto que creemos
class Naves():
    peso = 2500
    color = "Negro"
    activada = False
    def __init__(self,tamanho,asiento):
        self.tamanho = tamanho
        self.asiento = asiento
        self.ejecutar()
      

    def ejecutar(self):
        print("Esta en ejecucion")

    def encender(self):
        self.activada = True
    def comprobar(self):
        if(self.activada):
            print("Esta activado")
        else:
            print("Esta apagada")
obj1 = Naves("50.00",4)
obj1.tamanho = "60.00"

# del obj1.tamanho
# del obj1
print(obj1.tamanho, obj1.color) 
#nave1.encender()
#print(nave1.comprobar())
class Nave_Ultra(Naves):
    def __init__(self, tamanho, asiento,cantgasolina):
        super().__init__(tamanho,asiento)
        self.cantgasolina = cantgasolina
    def descripcion(self):
        print(f"Tam: {self.tamanho} Asiento: {self.asiento} Gasolina: {self.cantgasolina}")
objU = Nave_Ultra("60.00",5,400)
objU.descripcion()
# Las funcion puede agarrar variables de afuera.(Variables globales)
# Global para hacer globales las varias locales
vag = "VariableG"
def fu1():
    global va 
    va = "Variable"
    print(vag)
    def fu2():
        print(va)
    fu2()
fu1()
def fu3():
    print(va)
fu3()
# Importar Modulos(ficharo) y lamba sirve para funciones cortas que ocupe una linea
import math
def area(radio):
    resultado = math.pi * radio * radio
    print(round(resultado,2))
area(2)
area = lambda radio: round(math.pi * radio * radio)
print(area(2))
nombre = lambda nombre,apellido : print(f"Nombre y Apellido: {nombre} y {apellido}")
nombre("Miguel","Torres")
# fechas
import datetime,locale
locale.setlocale(locale.LC_ALL,"es-ES")
fecha = datetime.datetime.now()
print(f"Año:{fecha.year} Mes :{fecha.month} Dia:{fecha.day}")
print(fecha.strftime("%A"),fecha.strftime("%d"),fecha.strftime("%w"),
      fecha.strftime("%B"),fecha.strftime("%m"),fecha.strftime("%Y"),
      fecha.strftime("%H"),fecha.strftime("%j"),fecha.strftime("%c"))
#Expresiones Regulares:
# search : si encuentra en formato tupla recuelve la posicion inicial y final y no encuentra
# devuelve none
import re
tex = "MARIA223411567891234567891324"
print(re.search(" ",tex))
#FINDALL encuentra todo la cantidad de caracter que le indiques
print(re.findall("1",tex))
# split() y sub()
print(re.split("115",tex)) 
print(re.split("1",tex,1))
print(re.sub("1","maria",tex,1))
# SECUENCUAS ESPECIALES,METACARACTERES Y SETS
# \A1  devuelve una concidencia si los caracteres especificado esta al principio de la cadena
# \D devuelve una concidencia donde la cadena no contiene digitos
# {} ESPECIFICAR UN SET DE CARACTER A BUSCAR
# \ INDICA QUE SEGUIDO DE ELLA HAY UNA SECUENCIA ESPECIAL . SUSTITUIR CUALQUIER CARACTER QUE ALLA
print(re.findall("\D",tex))
print(re.findall("..RIA..",tex))
print(re.findall("[A-R]",tex))
#  ValueError : Evalua los errores con tipos de datos erroneos
"""try:
    variable = int(input("Colocar: "))
except ValueError:
    print("Hay un error")
else:
    print("N")"""
# Orientada Objetos:
class Vehiculo():
    pais_o = "Alemania"
    def __init__(self,color,l_m,r):
        self.color = color
        self.long_met = l_m
        self.ruedas = r
    def arrancar(self):
        print("Arrancando")
    def descr(self):
        print(f"Color: {self.color} and Pais: {self.pais_o} Precio:{self.precio}")
v1 = Vehiculo("Rojo","400",4)
v1.precio = 2700
v1.descr()


