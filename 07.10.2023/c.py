# Napisać metodę pour_out_liquid(requested_amount: float) -> tuple[str,float]
# która pozwala na wylanie części lub całego napoju z kubka

class Mug:
    
    def __init__(self, color, capacity, content_amount: float, content_type: str):
        print('uruchamiam konstruktor klasy A')
        self.color = color #pole
        self.capacity = capacity
        self.content_amount = content_amount
        self.content_type = content_type
    
    def get_content_type(self):
        return self.content_type
    
    def get_content_amount(self):
        return self.content_amount
    
    def fill(self, content_type: str, content_amount: float):
        if (content_type == self.content_type and content_amount + self.content_amount <= self.capacity):
            self.content_amount = self.content_amount + content_amount
            self.content_type = content_type
            return True
        else:
            return False
        
    def pour_out_liquid(self,requested_amount: float) -> tuple[str,float]:
        if (self.content_amount - requested_amount == 0):
            self.content_type = None
            return [self.content_type,requested_amount]
        if (self.content_amount - requested_amount < 0):
            self.content_type = None
            return [self.content_type,self.content_amount]
        if (self.content_amount - requested_amount > 0):
            return [self.content_type,requested_amount]
    
#tworzenie instancji
a = Mug('Red',500,300,'cola')

print(a.get_content_amount())
print(a.fill('cola',300))
print(a.pour_out_liquid(200))