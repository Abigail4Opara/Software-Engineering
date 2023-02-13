class Circle(object):

    def __init__(self, radius):
        self.radius =float(radius)

    def areaofCircle(self, radius):
        pi = 3.14159
        return(pi*radius**2)
    def circumferenceofCircle(self,radius):
        pi = 3.14159
        return(2*pi*radius)

user_radius = float(input("Kindly input the radius...:"))
userCircle = Circle(user_radius)
userCircle.radius = user_radius
print("The Area of the Circle is:",userCircle.areaofCircle(user_radius))
print("The Circumference of the Circle is:",userCircle.circumferenceofCircle(user_radius))       
    