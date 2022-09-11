"""
VECTOR 1 DIMENSION 
vector = [2, 3, 4, 5]

VECTOR 2 DIMENSIONES (filas - columnas I)
      0  1  2  3  4
  0 [ 2, 3 ,3 ,4 ,4 ] -> fila 
  1 [ 3, 4, 9, 6, 8 ]
  2 [ 3, 4, 5, 6, 7 ]
  3 [ 3, 4, 9, 4, 2 ]
  4 [ 3, 4, 5, 6, 9 ]
  5 [ 3, 4, 9, 7, 7 ]
  6 [ 3, 4, 5, 6, 8 ]
    columnas 

CONSTRUCCIÓN DE UNA MATRIZ
  semana1 = [ 2, 3 ,3 ,4 ,4 ]
  semana2 = [ 3, 4, 9, 6, 8 ]
  matrizSemanas = [semana1, semana2]

ACCEDER A UN DATO DE UNA MATRIZ
  print(semanas[0]) -> [ 2, 3 ,3 ,4 ,4 ]
  print(semanas[0][4]) -> 4

TIPOS DE DATOS
  sting = ""
  int = 0
  float = 0.0
  objecto = {
    "nombre": "pipe",
    "edad": 23,
  }
  list = ["", 0 , 0.0, object]

  CICLO FOR IN
    indice    0   1     2     3   4    5
  semana1 = [100, 200, 300, 400, 500, 600]
  semana2 = [100, 200, 300, 400, 500]

  for i in range(0, len(semana1)):
    print("semana1[", i, "] = ", semana1[i])

  for dia in semana1:
    print(dia)
"""