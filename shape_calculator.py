import math
from ntpath import join

 
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'    
        
    def set_width(self, width):
        self.width=width    

    def set_height(self, height):
        self.height=height
        
    def get_area(self):
        return self.height * self.width
        #print(f'the area is {self.height * self.width}')
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
        
    def get_diagonal(self): 
        return pow(pow(self.width, 2) + pow(self.height, 2 ), 0.5)   
        
    def get_picture(self):
        
        if self.width > 50  or self.height > 50:
            return 'Too big for picture.'
        
        # j=''
        # for i in range (self.height):
        #     j+='*'* self.width+'\n'
        # return j  
        
        #solucion 2 
          
        #acontinucion hice un ciclo "for" anidado:    
        for i in range(1, self.height+1):# este ciclo for es el que controla el altura de las columnas
            for x in range(1, self.width+1):# este ciclo for es el que controla la ancho  de las filas
                print("*", end="")
            print(" ")
        #else:
            #raise Exception ("se shompio")
        
    def get_amount_inside(self, figure):
        
        return self.get_area()//figure.get_area()
        
        
                  
                    
class Square(Rectangle):
    
    def __init__(self, large):
        super().__init__(large, large)
   
        
    def __str__(self) -> str:
        return f'Square(side={self.width})' 
        
    
    def set_side(self, large):
        self.width=large
        self.height=large
        
    # def set_width(self, width):
    #     return self.set_width(width)
    
    # def set_height(self, height):
    #     return self.set_height(height)    
    

