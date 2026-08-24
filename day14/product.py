class Product:
    """
    name  → self.name
    price → self._price
    stock → self.stock
    """
    def __init__(self, name, price, stock):
        self.name = name
        self._price = price
        self.stock = stock

    """
    外部可以：
    apple.price 
    """
    @property
    def price(self):
        return self._price

    """
    value < 0
    ↓
    raise ValueError("Price cannot be negative")
    
    否则
        ↓
    self._price = value
    """
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        else:
            self._price = value

    """
    quantity <= 0
    ↓
    raise ValueError("Quantity must be greater than 0")
    
    quantity > stock
        ↓
    return None
    
    否则
        ↓
    stock -= quantity
        ↓
    return price * quantity
    """
    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        elif quantity > self.stock:
            return None
        else:
            self.stock -= quantity
            return self.price * quantity

    """
    apple = Product("apple", 5, 10)
    apple.show_info()
    
    apple - Price: 5, Stock: 10
    """
    def show_info(self):
        print(f"{self.name} - Price: {self.price}, Stock: {self.stock}")



