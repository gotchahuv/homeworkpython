from abc import ABC, abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def sh_area(self):
        print('ploshad',self.area())
    @abstractmethod
    def perimeter(self):
        pass
    def sh_per(self):
        print('perimeter',self.perimeter())
    @abstractmethod
    def opis(self):
        pass
    def sh_opis(self):
        print('opis',self.opis())
class Rectangle(shape):
    def __init__(self,a,b):
        if not all(isinstance(x, (int, float)) and math.isfinite(x) and x > 0 for x in (a,b)):
            raise ValueError('Неверные стороны')
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeter(self):
        return 2*(self.a+self.b)
    def opis(self):
        return "ПРЯМОУГОЛЬНИК"
class Circle(shape):
    def __init__(self,r):
        if not isinstance(r, (int, float)) or not math.isfinite(r) or r <= 0:
            raise ValueError('Неверный радиус')
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def perimeter(self):
        return 2*math.pi*self.r
    def opis(self):
        return "КРУГ"
class Triangle(shape):
    def __init__(self,a,b,c):
        if not all(isinstance(x, (int, float)) and math.isfinite(x) and x > 0 for x in (a, b, c)):
            raise ValueError('Неверные стороны')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Такого треугольника нет')
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return self.a*self.b*self.c
    def perimeter(self):
        return self.a+self.b+self.c
    def opis(self):
        return "треугольник"
figur=[Rectangle(3,4),Circle(4),Triangle(4,4,5)]
sum_s=0
for i in figur:
    i.sh_opis()
    i.sh_area()
    i.sh_per()
print('Общая площадь',sum_s)