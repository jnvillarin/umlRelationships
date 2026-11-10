#Dependency
class PaymentService:
    def charge(self, amount):
        print(f"Charged ${amount}")
 
 
class Order:
    def __init__(self, total):
        self.total = total
 
    # PaymentService is only a method parameter: it is NOT stored as an attribute
    def pay(self, service):
        service.charge(self.total)
 
 
order = Order(49.99)
order.pay(PaymentService())