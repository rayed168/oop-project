radius=int(input("Enter the radius of the circle : "))
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
Circle1=Circle(radius)
print("The area of the circle is : ",Circle1.area())
print("The perimeter of the circle is : ",Circle1.perimeter())