cart = []

while True:
    item = input("Enter item (or type 'done' to stop): ")
    
    if item.lower() == "done":
        break
    
    cart.append(item)

print("Your cart items:")
for item in cart:
    print("-", item)