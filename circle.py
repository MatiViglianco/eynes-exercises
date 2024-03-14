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