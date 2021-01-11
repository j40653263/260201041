from math import pi

class Cylinder:
    def __init__(self,radius,height):
      self.radius = radius 
      self.height = height
    
    def get_radius(self):
      return self.radius
        
    def get_height(self):
      return self.height
    
    def set_radius(self,radius):
      self.radius =radius
    
    def set_height(self,height):
      if height > 0 :
        self.height = height
            
    def calculate_area(self):
      return 2 * self.calculate_base_area() + self.calculate_surface_area()
    
    def calculate_base_area(self):
      return pi * (self.radius) ** 2
    
    def calculate_surface_area(self):
      return 2 * pi * self.radius * self.height
    
    def calculate_volume(self):
      return self.calculate_base_area() * self.height
    
c = Cylinder(3, 5)
print("Area:",c.calculate_area())
print("Volume:",c.calculate_volume())