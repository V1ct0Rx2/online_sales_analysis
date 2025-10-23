
from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()
    
    
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.49, 25)
    product3 = Product("Headphones", 79.99, 50)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    
    manager.display_all_products()
    
    
    total_value = manager.total_inventory_value()
    print(f"\n Total Inventory Value: ${total_value:.2f}")
    
if __name__ == "__main__":
    main()