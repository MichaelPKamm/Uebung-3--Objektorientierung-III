#Uebung 3

import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


#-----------------------------------


class Figur:
    def __init__(self, name):
        self.name = name

    def umfang(self):
        return 0

    def __str__(self):
        return self.name



class Dreieck(Figur):
    def __init__(self, punkt1, punkt2, punkt3):
        super().__init__("Dreieck")
        self.punkt1 = punkt1
        self.punkt2 = punkt2
        self.punkt3 = punkt3

    def umfang(self):
        seite1 = ((self.punkt1.x - self.punkt2.x) ** 2 + (self.punkt1.y - self.punkt2.y) ** 2) ** 0.5
        seite2 = ((self.punkt2.x - self.punkt3.x) ** 2 + (self.punkt2.y - self.punkt3.y) ** 2) ** 0.5
        seite3 = ((self.punkt3.x - self.punkt1.x) ** 2 + (self.punkt3.y - self.punkt1.y) ** 2) ** 0.5
        return seite1 + seite2 + seite3

    def __str__(self):
        return f"{self.name} A={self.punkt1}, B={self.punkt2}, C={self.punkt3}"


class Rechteck(Figur):
    def __init__(self, ecke1, ecke2):
        super().__init__("Rechteck")
        self.ecke1 = ecke1
        self.ecke2 = ecke2

    def umfang(self):
        return 2*(abs(self.ecke2.x - self.ecke1.x)+abs(self.ecke2.y-self.ecke1.y))
    
    def __str__(self):
        return f"{self.name}, {self.ecke1} - {self.ecke2}"


class Kreis(Figur):
    def __init__(self, Mittelpunkt, Radius):
        super().__init__("Kreis")
        self.m = Mittelpunkt
        self.r = Radius

    def umfang(self):
        return 2*math.pi*self.r
    
    def __str__(self):
        return f"{self.name} M={self.m} und R={self.r}"
    

class polygon(Figur):
    def __init__(self, punkte):
        super().__init__("Polygon")
        self.punkte = punkte

    def umfang(self):
        u = 0
        for i in range(1, len(self.punkte)):
            j = (i + 1)%(len(self.punkte))
            u = u + math.sqrt((self.punkte[j].x - self.punkte[i].x)**2 + 
                              (self.punkte[j].y - self.punkte[i].y)**2)
            return u
    
    def __str__(self):
        string = ', '.join(str(i) for i in self.punkte)
        return f"{self.name}, {string}"




A = Punkt(1, 2)
B = Punkt(3, 4)
C = Punkt (5, 6)

d = Dreieck(A, B, C)
print(d)
print(d.umfang())

e = Rechteck(A, B)
print(e)
print(e.umfang())

f = Kreis(A, 5)
print(f)
print(f.umfang())


g = [A, B, C]
h = polygon(g)
print(h)
print(h.umfang())


