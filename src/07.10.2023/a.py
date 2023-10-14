# Stworzyć klasę "Mug" (kubek); powinna mieć pola "color, capacity, content_amount: float, content_type: str"

class Mug:
    
    def __init__(self, color, capacity, content_amount: float, content_type: str):
        print('uruchamiam konstruktor klasy A')
        self.color = color #pole
        self.capacity = capacity
        self.content_amount = content_amount
        self.content_type = content_type
    
    def foo(self): #metoda
        return f'Color: {self.color}, Capacity: {self.capacity}L, Amount: {self.content_amount}L, Type: {self.content_type}'
    
    
#tworzenie instancji
a = Mug('Red',2,1,'cola')


print(a.foo())
