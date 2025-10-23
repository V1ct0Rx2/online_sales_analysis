
from product import Product
from product_manager import ProductManager
from cart import Cart
import random


def main():
    manager = ProductManager()
    
    
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.49, 25)
    product3 = Product("Headphones", 79.99, 50)
    product4  = Product("Monitor", 199.99, 15)
    product5  = Product("Keyboard", 49.99, 30)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)
    manager.add_product(product5)
    
    
    manager.display_all_products()
    
    cart = Cart()
    
    selected_products = random.sample(manager.products, 3)
    for prod in selected_products:
        cart.add_to_cart(prod)
    
    total_value = cart.total_cart_value()
    print(f"\n Total cart value: ${total_value:.2f}")
    
    
if __name__ == "__main__":
    main()