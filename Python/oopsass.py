class Area():
   def area1(self):
      print(' Area of rectangle',self.l*self.b)
class Area2(Area):
    def __init__(self,length ,breadth, height):
       self.l=length
       self.b=breadth
       self.h=height
    def area1(self):
        print('area of triangle',0.5 *self.l*self.b)
    def volume(self):
        print('volume of rectangle',self.l*self.b*self.h)
        
obj=Area2(30,40,50)
obj.area1()
obj.volume()