class cone():
    def __init__(self, radius, height):
        self.radius=radius
        self.height=height



    def volume(self):
        volume=3.14* (self.radius**2)*self.height/3
        print("volume=", volume)
    
    def surface_area(self):
        l=(self.height**2 + self.radius**2)**(1/2)
        area= ((22/7) * self.radius)*(self.radius + l)
        print("area=", area)



        
dav=cone(2,4)
dav.volume()
dav.surface_area()
















