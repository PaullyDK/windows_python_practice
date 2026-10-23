code = ''
while code != "2026":
    code = input("Enter a 4 digit pin: ")
    if code == 'exit':
        exit()
if code == "2026":
    print("Success! We will proceed.")
    prices = eval(input("Enter a list of item prices."))
    total_sum = 0
    for price in prices:
        if price <= 0:
            print("invalid")
        elif price > 500:
            print("insurance review is required")
            break
        else:
            total_sum += price
    else:
        print("congratulations!")
        total_sum *= .9
    counter = int(input("Give me a small number."))
    for i in range(counter):
        for j in range(counter):
            if i == j:
                pass  # Explicitly fulfills the 'pass' requirement
            else:
                print(f"({i},{j})", end=" ")
        print()

    del prices
    

