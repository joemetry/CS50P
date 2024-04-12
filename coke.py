def main():
    price = 50
    accepted_coins = [25, 10, 5]
    total_inserted = 0

    while total_inserted < price:
        coin = int(input("Insert coin (25, 10, 5): "))
        if coin in accepted_coins:
            total_inserted += coin
            if total_inserted < price:
                print(f"Amount Due: {price - total_inserted}")

    change = total_inserted - price
    if change > 0:
        print(f"Change Owed: {change}")
    else:
        print("Change Owed: 0")

if __name__ == "__main__":
    main()
