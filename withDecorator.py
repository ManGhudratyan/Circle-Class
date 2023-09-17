class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            print("Radius cannot be negative")

circle = Circle(5)

print("Radius:", circle.radius)

circle.radius = 7
print("Updated Radius:", circle.radius)

circle.radius = -2

