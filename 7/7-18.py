sandwich_orders = ["sandwich","三明治","sadas"]
finish_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(" I will made "+current_sandwich)
    finish_sandwiches.append(current_sandwich)

for sandwish in finish_sandwiches:
    print(sandwish)
