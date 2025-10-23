
from product import Product

class Cart:
    def __init__(self):
        
        self.cart_items = []
        
    def add_to_cart(self, product: Product):
        
        self.cart_items.append(product)
        print(f"Added '{product.name}' to cart.")
        
    def display_cart(self):
        
        if not self.cart_items:
            print("Your cart is empty.")
            return
        print("\n--- Items in your cart ---")
        
        for item in self.cart_items:
            print(item.display_info())
        print("--------------------------\n")
        
    def total_cart_value(self):
        
        total_value = sum(item.price * item.quantity for item in self.cart_items)
        return total_value
        