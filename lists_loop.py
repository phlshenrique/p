sandwich_orders = ['x-egg', 'Pastrami', 'cheese burger', 'pasTrami', 'cheddar mc melt', 'pastramI', 'cbo', 'chicken mc junior']
finished_sandwiches = []
print("We ran out of Pastrami, if you ordered one, it will not be made")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich.lower() == 'pastrami':
        print("\nI told you we run out of Pastrami, the order will not be made")
        continue
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nThere we go! - Here are all the sandwiches that were made:\n")
for sandwich in finished_sandwiches:
    print(sandwich)
