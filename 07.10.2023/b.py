# Napisać metody: get_content_type(), get_content_amount(), fill(content_type: str, content_amount: float), 
# przy czym ta ostatnia ma sprawdzać 
# w przypadku dolewania czy dolewamy tego samego typu cieczy, i czy nie przekraczamy maksymalnego amount (lub zera)

class Mug:
    
    def __init__(self, color, capacity, content_amount: float, content_type: str):
        print('uruchamiam konstruktor klasy A')
        self.color = 'red' #pole
        self.capacity = 400
        self.content_amount = 100
        self.content_type = 'cola'
    
    def get_content_type(self):
        return self.content_type
    
    def get_content_amount(self):
        return self.content_amount
    
    def fill(self, content_type: str, content_amount: float):
        if (content_type == self.content_type and content_amount + self.content_amount <= self.capacity):
            return True
        else:
            return False
        
#tworzenie instancji
a = Mug('Red',2,1,'cola')



print(a.fill('cola',200))