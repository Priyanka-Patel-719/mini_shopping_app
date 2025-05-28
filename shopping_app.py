product_catalog = {
    1: ("Apple", 10),
    2: ("Banana", 5),
    3: ("Milk", 20),
    4: ("Bread", 15),
    5: ("Butter", 25)
}

categories = {"Fruits", "Dairy", "Bakery"}

cart = {}

while True:
    print("\n========= MINI SHOPPING APP =========")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print("\n🛒 Available Products:")
        for pid in product_catalog:
            name, price = product_catalog[pid]
            print(f"{pid}. {name} - ₹{price}")

    elif choice == '2':
        pid = int(input("Enter product ID to add: "))
        qty = int(input("Enter quantity: "))

        if pid in product_catalog:
            name = product_catalog[pid][0]
            if name in cart:
                cart[name] += qty
            else:
                cart[name] = qty
            print(f" {qty} x {name} added to cart.")
        else:
            print(" Invalid product ID.")

    elif choice == '3':
        item = input("Enter product name to remove: ").title()
        if item in cart:
            cart.pop(item)
            print(f"{item} removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == '4':
        if not cart:
            print("Your cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for item in cart:
                qty = cart[item]
                # Get price from catalog
                for (n, p) in product_catalog.values():
                    if n == item:
                        price = p
                        break
                item_total = price * qty
                total += item_total
                print(f"{item}: {qty} x {price} = ₹{item_total}")
            print(f"Total Amount: ₹{total}")

    elif choice == '5':
        if not cart:
            print("Cart is empty. Add items first.")
        else:
            print("\nFinal Cart:")
            total = 0
            for item in cart:
                qty = cart[item]
                for (n, p) in product_catalog.values():
                    if n == item:
                        price = p
                        break
                item_total = price * qty
                total += item_total
                print(f"{item}: {qty} x ₹{price} = ₹{item_total}")
            print(f"Total Amount: ₹{total}")
            confirm = input("Proceed to checkout? (yes/no): ")
            if confirm.lower() == "yes":
                print("Checkout successful! Thank you for shopping")
                cart.clear()
            else:
                print("Checkout cancelled.")

    elif choice == '6':
        print("Goodbye! Come again.")
        break

    else:
        print("Invalid choice. Try again.")
