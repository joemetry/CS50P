import sys
import requests

def main():
    # Check for command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py AMOUNT")

    # Convert the argument to a float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number")

    # Query the CoinDesk API for the current price of Bitcoin
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        rate = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Could not retrieve data from CoinDesk API")

    # Calculate and output the cost of the specified amount of Bitcoin
    cost = amount * rate
    print(f"The cost of {amount} Bitcoin(s) is ${cost:,.4f}")

if __name__ == "__main__":
    main()
