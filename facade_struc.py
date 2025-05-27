# Facade Design Pattern is a structural design pattern that provides a simplified interface to a complex system, encapsulating the complexities of multiple subsystems into a single unified interface for clients. 

# Naive solution

class OrderRequest:
    def __init__(self):
        self.name = "danny"
        self.card_number = "1234"
        self.amount = 20.99
        self.address = "123 Springfield Avenue, Texas"
        # Item ids user want to offer
        self.item_ids = ["123","423","555","989"]

class Authenticator:
    def authenticate(self) -> bool:
        return True 

class Inventory:
    def check_inventory(self,item_id : "str") -> bool:
        return True
    
    def reduce_inventory(self,item_id : str,amount : int) -> bool:
        print(f"Reducing Inventory of {item_id} by {amount}")


class Payment:
    def __init__(self,name :str,card_number : str, amount:int):
        self._name = name
        self._card_number = card_number
        self._amount = amount
    
    def pay(self):
        print(f"Charging card with name: {self._name} ")

class OrderFulfilment:
    def __init__(self,inventory:Inventory):
        # Protected Attribute to hold the inventory instance
        self._inventory = inventory

    def fulfill(self, name: str ,addrees: str , items : list[str] ):
        print("Inserting order into database")
        for item in items:
            self._inventory.reduce_inventory(item,1)

# Order request contains info that the user has submitted while making the order 

order_req = OrderRequest()

auth = Authenticator()
auth.authenticate

inventory = Inventory()
for item_id in order_req.item_ids:
    inventory.check_inventory(item_id)

payment = Payment(order_req.name,order_req.card_number,order_req.amount)
payment.pay()

order_fulfillment = OrderFulfilment(inventory)
order_fulfillment.fulfill(order_req.name,order_req.address,order_req.item_ids)

# Here each client who needs to make an order is dependent on four classes. So if you have to make 10 orders then 10 classes needs to be made. Also if there is an update in any of the four classes then we may need to update the 10 classes. So, the solution to this is facade pattern.

# Remember for client making an order he does not need to know about the steps involved in making an order. He only needs to make an order. So we can make a new class called OrderService with one method that abstracts all the logic so that all the classes which need to make an order only have to depend on this one class called Order Service class. 

# Refactored Solution

class OrderRequest:
    def __init__(self):
        self.name = "danny"
        self.card_number = "1234"
        self.amount = 20.99
        self.address = "123 Springfield Avenue, Texas"
        # Item ids user want to offer
        self.item_ids = ["123","423","555","989"]

class Authenticator:
    def authenticate(self) -> bool:
        return True 

class Inventory:
    def check_inventory(self,item_id : "str") -> bool:
        return True
    
    def reduce_inventory(self,item_id : str,amount : int) -> bool:
        print(f"Reducing Inventory of {item_id} by {amount}")


class Payment:
    def __init__(self,name :str,card_number : str, amount:int):
        self._name = name
        self._card_number = card_number
        self._amount = amount
    
    def pay(self):
        print(f"Charging card with name: {self._name} ")

class OrderFulfilment:
    def __init__(self,inventory:Inventory):
        # Protected Attribute to hold the inventory instance
        self._inventory = inventory

    def fulfill(self, name: str ,addrees: str , items : list[str] ):
        print("Inserting order into database")
        for item in items:
            self._inventory.reduce_inventory(item,1)

class OrderService:
    def create(self,order_request):
        auth = Authenticator()
        auth.authenticate

        inventory = Inventory()
        for item_id in order_req.item_ids:
            inventory.check_inventory(item_id)

        payment = Payment(order_req.name,order_req.card_number,order_req.amount)
        payment.pay()

        order_fulfillment = OrderFulfilment(inventory)
        order_fulfillment.fulfill(order_req.name,order_req.address,order_req.item_ids)



# Order request contains info that the user has submitted while making the order 

order_req = OrderRequest()
order_service = OrderService()
order_service.create(order_req)

# So the advantage of this program is that all clients can make order without having to depend on many classes and without having to know many of the complexities. As they have been abstracted away and encapsulated in OrderService class. 