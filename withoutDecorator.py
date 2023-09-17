class Circle:
    def __init__(self, radius):
        self.__radius = radius;
    
    def get_radius(self):
        return self.__radius;
    
    def set_radius(self, radius):
        if (radius >= 0):
            self.__radius = radius;
        else:
            print('Its a negative number');

circle = Circle(5)

print("Radius:", circle.get_radius())

circle.set_radius(7)
print("Updated Radius:", circle.get_radius())

circle.set_radius(-2)
