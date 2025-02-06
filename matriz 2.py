Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> maxf = 3
... maxc = 5
... a = [[0.0] * maxc for _ in range (maxf)]
... 
... 
... #leer el array
... for f in range (maxf):
...     for c in range (maxc):
...         print("ingrese un valor: ")
...         a[f][c] = float(input())
... 
... 
...     #escribir el array
...     print("impresion de valores almacenados")
...     for f in range (maxf):
...         for c in range (maxc):
...             print(a[f][c], end=" ")
...             print()
