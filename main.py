
from product import Product
from product_manager import ProductManager
from cart import Cart
import random


def main():
    manager = ProductManager()
    
    

    product1 = Product("Tablet", 90.99, 20)
    product2 = Product("Smartwatch", 199.99, 19)
    product3 = Product("Camera", 299.99, 15)
    product4 = Product("Laptop", 999.99, 10)
    product5 = Product("Smartphone", 499.49, 25)

    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)
    manager.add_product(product5)
    
     
    cart = Cart()
    
    selected_products = random.sample(manager.products, 3)
    for prod in selected_products:
        cart.add_to_cart(prod)
    
    cart.display_cart()
    total_value = cart.total_cart_value()
    print(f"\n Total cart value: ${total_value:.2f}")
    
    

if __name__ == "__main__":
    main()