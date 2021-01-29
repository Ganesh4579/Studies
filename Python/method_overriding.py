class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer
        
    def __len__(self):
        return len(self.cart)



order = Order(['banana', 'apple', 'mango'], 'Real Python')
print(len(order))
l=list('qwejhgjh')
print(len(l))