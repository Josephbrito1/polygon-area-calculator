import math
# def get_picture(width, height):
        
#     if width > height and width < 50  and height <50:
#         #acontinucion hice un ciclo "for" anidado:    
#         for i in range(1, height+1):# este ciclo for es el que controla el altura de las columnas
#             for x in range(1, width+1):# este ciclo for es el que controla la ancho  de las filas
#                 print("*", end="")
#             print(" ")
#     else:
#         raise Exception ("se shompio")
    
# print(get_picture(5, 20))

height=2
width=2

for i in range(1, height+1):# este ciclo for es el que controla el altura de las columnas
    for x in range(1, width+1):# este ciclo for es el que controla la ancho  de las filas
        print("*", end="")
    print(' ')
          