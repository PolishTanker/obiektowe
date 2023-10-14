# klasa --- ma "pola (feilds) i metody/funkcje"

class Robot:
    
    def __init__(self, name: str):
        print('uruchamiam konstruktor klasy A')
        self.name = name #pole
    
    def foo(self): #metoda
        return f'my name is {self.name}'
    
    def add(self, a: int, b: int):
        return a + b
    
#tworzenie instancji
a = Robot('Xiao')

#tworzenie drugiej instancji
b = Robot('Li')

print(a.foo())
print(b.foo())