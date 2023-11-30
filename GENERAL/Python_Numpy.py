"""import array as a
matriz = a.array('i',[1,2])"""
import numpy as np
lista  = [[1,2,3],[4,5,6]]
matriz = np.array([1,2,3])
matriz1 = np.array(lista)
print(matriz1 * matriz)
print(matriz[0])
m = np.arange(1,10,2).reshape(1,5)
print(m)
# llamar a la variable shape para saber cuantas filas y columnas contiene.
print(f'Indica cuantas filas  y columnas contiene {m.shape}')
print(f'Dimensiones: {m.ndim}')
print(f'Cantidad de elementos: {m.size}')
# Algebra lineal , matrices unicamente compuesta con el valor de 0
l = np.zeros((3,4))
print(l)
l1 = np.linspace(80,90,10)
print(l1)
print(l1.size)
# Una matriz de 3 dimensiones
l2 = np.arange(12).reshape(2,3,2)
print(l2)
# OPERACIONES CON MATRICES
l3 = np.array([
    [1,2,15],
    [4,2,8] ]
)
l4 = np.array([
    [90,100,110],
    [120,130,140] ]
)
print(np.sort(l3))
#Elevado a la potencia de un numero
p = np.power(l3,3)
print(np.sort(p))
print(np.array(l3**3))
print(np.array(l3 >= 4 ))
print(np.array(l3.max()))
print(np.array(l3.min()))
#print(np.concatenate((l3,l4)))
#print(np.add(l3,l4))
#print(np.subtract(l3,l4))
#print(np.multiply(l3,l4))
#print(np.divide(l3,l4))
# Como usar los numeros aleatorios
l6 = np.random.randint(5,size=(5));
l7 = np.random.rand(3,3)
print(l6)
print(l7)
# Obtiene un valor del array colocado como parametro
l8 = np.random.choice([120,130,140],size=(1,3))
print(l8)
l9 = np.random.choice\
    ([2,4,8,10],p=[0.25,0.25,0.25,0.25],size=(60))        
print(l9)
# Implementar ejes a las mastrices
# axis 0(y) horizontal: columna axis(x)1 vertical : fila
# Una sola dimension eje con el valor de 0
l10 = np.array([[0,1,2],[2,4,5]])
l11 = np.array([[10,11,2],[2,4,5]])
l12 = np.array([0,1,2])
l13 = np.array([10,11,2])
print(np.sum(l10, axis=1))
print(np.concatenate([l10,l11], axis=0))
print(np.concatenate([l10,l11], axis=1))
print(np.concatenate([l12,l13],axis=0))
print(np.sum([l12,l13],axis=0))
# funciones estadisticas
print(np.amax(l10,0))
print(np.amin(l10))
# 1:fila 0:columna(ejes)
#Rango de una matriz:Max - Min
print(np.ptp(l10,1))
# Percentiles =(Impar)q(n+1)/100 (Par)qxn/100
print(np.percentile(l10,100, axis=1))
print(np.median(l10,axis=1))
# Media aritmetica
print(np.mean(l10,axis=1))
l14 = [8,9,10]
# el promedio ponderado = x1*p1 + .. xn * Pn/ ΣP
# P: presenta un determinado peso, que tu mismo puedes asignar con un valor determinado.
# Por defecto el peso es el valor de 1
print(np.average(l14))
# Desviacion Estandar : D = √Σ|x - X̅| elevado al cuadrado/n
print(np.std(l14))
# Algebra lineal
m1 = np.array([
    [1,-1,2],
    [3,2,0],
])
print((np.transpose(m1)))
m2 = np.array([[1],[2],[3]])
print(np.transpose(m2))
# Matriz traspuesta: Es obtiene cambiando sus filas por columnas(o viceversa).
# Sistemas de ecuaciones Ax = b , buscamos la matriz de x
a = np.array([
    [2,1,-2],
    [3,0,1],
    [1,1,-1]
]);
b = np.array([[-3,5,-2]]); 
b1 = np.transpose(b)
x = np.linalg.solve(a,b1)
print(np.allclose(np.dot(a,x),b))

h1 = np.array([[2,7,3],[2,8,2],[1,3,1]])
h2 = np.array([1,1,0])
h2.shape = (3,1)
print(np.linalg.solve(h1,h2))


l = np.zeros((3,4))
print(l)