# Welcome message (personal touch)
print("Welcome to Ansh's Restaurant System 🍽️")

# ================== MENU AND INVENTORY ==================

# menu data contains item details
menu_data = {
    "Paneer Tikka": {"category": "Starters", "price": 180, "available": True},
    "Chicken Wings": {"category": "Starters", "price": 220, "available": False},
    "Veg Soup": {"category": "Starters", "price": 120, "available": True},
    "Butter Chicken": {"category": "Mains", "price": 320, "available": True},
    "Dal Tadka": {"category": "Mains", "price": 180, "available": True},
    "Veg Biryani": {"category": "Mains", "price": 250, "available": True},
    "Garlic Naan": {"category": "Mains", "price": 40, "available": True},
    "Gulab Jamun": {"category": "Desserts", "price": 90, "available": True},
    "Rasgulla": {"category": "Desserts", "price": 80, "available": True},
    "Ice Cream": {"category": "Desserts", "price": 110, "available": False},
}

# stock data for inventory tracking
stock_data = {
    "Paneer Tikka": {"stock": 10, "reorder": 3},
    "Chicken Wings": {"stock": 8, "reorder": 2},
    "Veg Soup": {"stock": 15, "reorder": 5},
    "Butter Chicken": {"stock": 12, "reorder": 4},
    "Dal Tadka": {"stock": 20, "reorder": 5},
    "Veg Biryani": {"stock": 6, "reorder": 3},
    "Garlic Naan": {"stock": 30, "reorder": 10},
    "Gulab Jamun": {"stock": 5, "reorder": 2},
    "Rasgulla": {"stock": 4, "reorder": 3},
    "Ice Cream": {"stock": 7, "reorder": 4},
}

# ================== TASK 1: ORDER SYSTEM ==================

print("\n===== SIMPLE ORDER SYSTEM =====")

my_orders = []      # stores ordered items
total_price = 0     # total bill amount

# loop until user types 'done'
while True:
    try:
        user_item = input("Enter item (type 'done' to stop): ").strip()
    except Exception as e:
        print("Input error:", e)
        continue

    # stop condition
    if user_item.lower() == "done":
        break

    # check if item exists
    if user_item not in menu_data:
        print("Item not found")
        continue

    # check availability
    if not menu_data[user_item]["available"]:
        print("Item currently unavailable")
        continue

    # check stock
    if stock_data[user_item]["stock"] <= 0:
        print("Out of stock")
        continue

    # add item to order
    my_orders.append(user_item)
    total_price += menu_data[user_item]["price"]

    # reduce stock after order
    stock_data[user_item]["stock"] -= 1

    print(user_item, "added")

print("\n--- BILL SUMMARY ---")

# print bill
if len(my_orders) == 0:
    print("No items ordered")
else:
    for it in my_orders:
        print(it)

    print("Total amount:", total_price)

# check items below reorder level
print("\nItems below reorder level:")
for item in stock_data:
    if stock_data[item]["stock"] <= stock_data[item]["reorder"]:
        print(item, "needs refill")


# ================== TASK 2: CART ==================

print("\n===== CART OPERATIONS =====")

my_cart = []  # list to store cart items

# function to add product into cart
def add_product(name, qty):
    # check if item exists
    if name not in menu_data:
        print("Not in menu")
        return

    # check availability
    if not menu_data[name]["available"]:
        print("Not available")
        return

    # check stock
    if stock_data[name]["stock"] < qty:
        print("Not enough stock")
        return

    found = False

    # check if item already exists in cart
    for obj in my_cart:
        if obj["item"] == name:
            obj["qty"] += qty
            found = True
            print("Quantity updated")

    # if new item, add to cart
    if not found:
        entry = {
            "item": name,
            "qty": qty,
            "price": menu_data[name]["price"]
        }
        my_cart.append(entry)
        print("Item added")

    # reduce stock
    stock_data[name]["stock"] -= qty


# function to remove item from cart
def remove_product(name):
    for obj in my_cart:
        if obj["item"] == name:
            my_cart.remove(obj)
            print("Item removed")
            return
    print("Item not in cart")


# display cart items
def display_cart():
    print("\nCurrent cart:")
    if len(my_cart) == 0:
        print("Cart is empty")
    else:
        for obj in my_cart:
            print(obj["item"], "x", obj["qty"])


# sample run
add_product("Paneer Tikka", 2)
add_product("Gulab Jamun", 1)
add_product("Paneer Tikka", 1)
remove_product("Gulab Jamun")
display_cart()

print("\n--- CART BILL ---")

subtotal = 0

# calculate bill
for obj in my_cart:
    item_total = obj["qty"] * obj["price"]
    subtotal += item_total
    print(obj["item"], "x", obj["qty"], "=", item_total)

# add tax
tax = subtotal * 0.05
final_amount = subtotal + tax

print("Subtotal:", subtotal)
print("Tax:", round(tax, 2))
print("Final amount:", round(final_amount, 2))


# ================== TASK 3: INVENTORY BACKUP ==================

import copy

print("\n===== INVENTORY BACKUP TEST =====")

# create deep copy backup
backup_copy = copy.deepcopy(stock_data)

# modify original data
stock_data["Paneer Tikka"]["stock"] = 2

print("Modified stock:", stock_data["Paneer Tikka"]["stock"])
print("Backup stock:", backup_copy["Paneer Tikka"]["stock"])

# restore original from backup
stock_data = copy.deepcopy(backup_copy)

print("Restored stock:", stock_data["Paneer Tikka"]["stock"])


# ================== TASK 4: SALES ANALYSIS ==================

sales_log = {
    "2025-01-01": [
        {"id": 1, "items": ["Paneer Tikka"], "total": 180},
        {"id": 2, "items": ["Veg Soup"], "total": 120},
    ],
    "2025-01-02": [
        {"id": 3, "items": ["Butter Chicken"], "total": 320},
    ],
}

print("\n===== DAILY SALES =====")

daily_total = {}

# calculate total revenue per day
for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]

    daily_total[date] = total
    print(date, ":", total)

# find best day
best_day = max(daily_total, key=daily_total.get)
print("Best day:", best_day)

item_count = {}

# count most ordered item
for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

top_item = max(item_count, key=item_count.get)
print("Most ordered item:", top_item)

# add new day
sales_log["2025-01-03"] = [
    {"id": 4, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270}
]

print("\nUpdated sales:")

# print updated sales
for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    print(date, "=", total)

print("\nProgram finished successfully")