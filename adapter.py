from abstract_factory import Rugs

class PriceAdapter:
    
    def __init__(self, rate):
        self.rate = rate
        
    def exchange(self, product_price):
        return self.rate * product_price
    
    
if __name__ == '__main__':
    r1 = Rugs('Tabriz', 50)
    r2 = Rugs('Mashahd', 45)
    r3 = Rugs('Esfehan', 49)
    
    adapter = PriceAdapter(28000)
    
    rug_products = [r1, r2, r3]
    
    for rug in rug_products:
        print(f"Rug name: {rug._name}\tRug Price: {adapter.exchange(rug._price)}")