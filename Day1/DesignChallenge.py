# Hotel Management System

# Menu
menu = {
    "Idli": 40,
    "Dosa": 60,
    "Poori": 50,
    "Fried Rice": 120,
    "Veg Biryani": 150,
    "Tea": 20,
    "Coffee": 30
}

print("========== WELCOME TO HOTEL ==========")
print("Menu")
print("--------------------------------------")
for item, price in menu.items():
    print(f"{item:15} Rs.{price}")
print("--------------------------------------")

bill = 0
order_list = []

while True:
    item = input("\nEnter item name: ")

    if item in menu:
        qty = int(input("Enter quantity: "))
        amount = menu[item] * qty
        bill += amount
        order_list.append((item, qty, amount))
        print(f"{item} added successfully!")
    else:
        print("Item not available!")

    choice = input("Do you want to order another item? (yes/no): ").lower()
    if choice != "yes":
        break

# GST Calculation
gst = bill * 0.18
total = bill + gst

# Print Bill
print("\n")
print("=========== HOTEL BILL ===========")
print("----------------------------------")
print("Item\t\tQty\tAmount")
print("----------------------------------")

for item, qty, amount in order_list:
    print(f"{item:15}{qty}\tRs.{amount}")

print("----------------------------------")
print(f"Subtotal : Rs.{bill:.2f}")
print(f"GST (18%): Rs.{gst:.2f}")
print("----------------------------------")
print(f"Total Bill: Rs.{total:.2f}")
print("==================================")
print("Thank You! Visit Again.")
