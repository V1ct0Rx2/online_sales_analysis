
from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()
    
    
    product1 = Product("Tablet", 90.99, 20)
    product2 = Product("Smartwatch", 199.99, 19)
    product3 = Product("Camera", 299.99, 15)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    
if __name__ == "__main__":
    main()