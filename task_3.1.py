import random

class Matrix:
   

    def __init__(self, lenght, height):
        self.l = lenght
        self.h = height
        self.matrix = [[1 for i in range(self.l)] for o in range(self.h)]
        
            
    def add_value(self, val):
        a = []
        for i in range(self.l - 1):
            a.append(1)
        a.append(val)
        self.matrix.append(a)
    
    def printy(self):
        g = self.matrix
        print(g)
   
    def quantity(self):
        count = 0
        for i in self.matrix:
            count += 1
            c = 0
            for k in i:
                c += 1
        print(f"Число строк: {count}")   
        print(f"Число столбцов: {c}") 
    def replace(self, ind, ex, rep):
        self.matrix[ind][ex] = rep
        


    

b = Matrix(5, 7)
b.printy()
b.add_value(5)
b.printy()
b.quantity()
b.replace(0, 1, 16)
b.printy()

    
    
