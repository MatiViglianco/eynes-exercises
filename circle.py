import math

class Circle():
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius            
        else:    
            raise ValueError("El radio no puede ser menor o igual a 0.")

    def get_radius(self):
        return self.radius

    def set_radius(self,radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("El radio no puede ser menor o igual a 0.")

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
    def get_perimeter(self):
        perimeter = math.pi * (self.radius * 2)
        return perimeter
    
    def __mul__(self, n):
        if n > 0:
            return Circle(self.radius * n)
        else:
            raise ValueError("El radio no puede ser menor o igual a 0.")
    
    def __str__(self):
        return f"EL círculo tiene un radio de {self.radius} unidades."