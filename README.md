# Online Sales Analysis

## Description
This Python project simulates an online sales system. It allows management of products, inventory, and customer carts. The project includes classes for products, inventory management, and shopping cart functionality.

## Classes

### Product
- Attributes: `name`, `price`, `quantity`
- Methods:
  - `display_info()` – Displays product details
  - `update_quantity(new_quantity)` – Updates the product quantity

### ProductManager
- Attribute: `products` (list of Product objects)
- Methods:
  - `add_product(product)` – Adds a product to inventory
  - `remove_product(name)` – Removes a product by name
  - `display_all_products()` – Shows all products
  - `total_inventory_value()` – Calculates total value of inventory

### Cart
- Attribute: `cart_items` (list of Product objects)
- Methods:
  - `add_to_cart(product)` – Adds product to cart
  - `display_cart()` – Shows cart contents
  - `total_cart_value()` – Calculates total price of cart items

## Usage
1. Create an instance of `ProductManager` and add products.
2. Create an instance of `Cart`.
3. Add products to the cart.
4. Display cart contents and total cart value.

## Notes
- Sensitive files like `config.json` and screenshots are ignored via `.gitignore`.

