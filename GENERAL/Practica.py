# EJERCICIO SUCESSION FIBONACCI:
num_uno,num_dos = 0,1
while num_dos <= 1597:
    print(num_uno, num_dos, end= " ")
    num_uno = num_uno + num_dos 
    num_dos = num_uno + num_dos
# ELIMINAR UNA PALABRA: LEN(): NOS PERMITE CONOCER LA LONGITUD DE UNA CADA DE CARACTERES
frase = "Siempre se puede cuando se quiere"
palabra = "cuando"
indice = frase.find(palabra)
substring = frase[0:indice] + frase[(indice + len(palabra) + 1): ]
print(f"\nPalabra elimina es '{palabra}' , quedando asi: '{substring}'")
# Invertir un string
frase_reversed = ""
for character in frase:
    frase_reversed = character + frase_reversed
print(f"Invertido: {frase_reversed}")
# TABLA DE MULTIPLICAR
tablamulti = 5
for indice in range(0,11):
    print(f"{tablamulti} * {indice} = {tablamulti * indice}")
# STRING SIN VOCALES:  
letraterminar_el_bucle = "c"
for character in frase:
    if character.lower() == letraterminar_el_bucle.lower():
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character,end="")
#Ejercicio manejo de LISTA:
"""Cantidadnumeroenteros =  5
Listanumerosenteros = []
for _ in range(0,Cantidadnumeroenteros,1):
    entero = int(input("Introduce un numero entero: "))
    Listanumerosenteros.append(entero)
print(f"\nLista: {Listanumerosenteros}")
print(f"Suma Total :  {sum(Listanumerosenteros)}") """
ListaOriginal = ['A','B','b','C']   
elemento = 'b'
for _ in ListaOriginal:
    if(elemento.lower() in ListaOriginal):
        ListaOriginal.remove(elemento.lower())
    elif(elemento.upper() in ListaOriginal):
        ListaOriginal.remove(elemento.upper())
print(f"Elemento eliminado : {ListaOriginal}")
"""for i in range(0,len(ListaOriginal),1):    
    if (elemento.lower() == ListaOriginal[i]):      
    elif(elemento.upper() == ListaOriginal[i]):
print(f"Elemento eliminado : {ListaOriginal}")"""
#
numerosO = [1,2,3,4,5]
numeros_eliminados = []
numeros_eliminados.append(numerosO.pop(0))
numeros_eliminados.append(numerosO.pop())
print(f'Numeros eliminados: {numeros_eliminados}, numeros : {numerosO}')
# EJERCICIO MATRIZ:
"""matrix = []
filasdematriz = 3
columnadematriz = 3
for filas in range(0,filasdematriz,1):
    fila = []
    for columna in range(0,columnadematriz,1):
        fila.append(input(f"Introduce un elemento a la fila {filas} columna {columna}: "))
    matrix.append(fila)
for row in matrix:
    for element in row:
        print(element, end= " ")
    print()
"""
# SUMA DE MATRICES
number_of_matrix = 2
if number_of_matrix > 1 :
    rows = 2
    columns = 2
    matrix_list = []
    
    for number in range(0,number_of_matrix,1):
        matrix = []
        for row in range(0,rows,1):
            new_row = []
            for column in range(0,columns,1):
                new_row.append(int(input(
                    f"Introduce un elemento para la matrix {number + 1} fila {row} columna {column}: "
                )))
            matrix.append(new_row)
        matrix_list.append(matrix)
    # Suma
    matrix = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            sum_matrix = 0
            for matrix_position in range(len(matrix_list)):
                sum_matrix += matrix_list[matrix_position][row][column]
            new_row.append(sum_matrix)
        matrix.append(new_row)
    matrix_list.append(matrix)
    #Imprimir
    for matrix_row in range(rows):
        for matrix_list_position in range(len(matrix_list)):
            if matrix_row != 1:
                print(f"{matrix_list[matrix_list_position][matrix_row]}", end="   ")
            else:
                if matrix_list_position < len(matrix_list) - 2:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" + ")
                elif matrix_list_position < len(matrix_list) - 1:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" = ")
                else:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end="   ")
        print()
else:
    print("Se necesita dos o mas matrices para realizar la suma")

