
inventory = {}


def add_product():
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")

    try:
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative!")
            return

    except ValueError:
        print("Invalid price or quantity!")
        return

    inventory[product_id] = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    print("Product added successfully!")


def view_products():
    if not inventory:
        print("Inventory is empty!")
        return

    print("\n---------- PRODUCT LIST ----------")

    for product in inventory.values():
        print(f"""
Product ID : {product['id']}
Name       : {product['name']}
Price      : ₹{product['price']:.2f}
Quantity   : {product['quantity']}
Category   : {product['category']}
-----------------------------------""")


def search_product():
    product_id = input("Enter Product ID to search: ")

    if product_id in inventory:
        product = inventory[product_id]

        print("\nProduct Found!")
        print("ID       :", product["id"])
        print("Name     :", product["name"])
        print("Price    : ₹", product["price"])
        print("Quantity :", product["quantity"])
        print("Category :", product["category"])
    else:
        print("Product not found!")


def update_quantity():
    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter new quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative!")
            return

        inventory[product_id]["quantity"] = quantity
        print("Quantity updated successfully!")

    except ValueError:
        print("Please enter a valid whole number!")


def delete_product():
    product_id = input("Enter Product ID to delete: ")

    if product_id in inventory:
        del inventory[product_id]
        print("Product deleted successfully!")
    else:
        print("Product not found!")


def low_stock_products():
    found = False

    print("\n---------- LOW STOCK PRODUCTS ----------")

    for product in inventory.values():
        if product["quantity"] < 5:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Quantity: {product['quantity']}"
            )
            found = True

    if not found:
        print("No low-stock products found!")


def total_inventory_value():
    total = 0

    print("\n---------- INVENTORY VALUE ----------")

    for product in inventory.values():
        value = product["price"] * product["quantity"]
        total += value

        print(
            f"{product['name']}: "
            f"₹{product['price']:.2f} x "
            f"{product['quantity']} = ₹{value:.2f}"
        )

    print("-------------------------------------")
    print(f"Total Inventory Value: ₹{total:.2f}")


def main():
    while True:
        print("""
=====================================
      INVENTORY MANAGEMENT SYSTEM
=====================================
1. Add Product
2. View Products
3. Search Product
4. Update Quantity
5. Delete Product
6. Show Low Stock Products
7. Show Total Inventory Value
8. Exit
=====================================""")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            low_stock_products()
        elif choice == "7":
            total_inventory_value()
        elif choice == "8":
            print("Thank you for using Inventory Management System!")
            break
        else:
            print("Invalid choice! Please select 1-8.")


if __name__ == "__main__":
    main()
