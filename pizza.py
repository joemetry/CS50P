import csv
import sys
from tabulate import tabulate

def read_pizza_csv(filename):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            pizza_list = [row for row in csv_reader]
            return pizza_list
    except FileNotFoundError:
        sys.exit(f"Error: {filename} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")
    elif not sys.argv[1].endswith('.csv'):
        sys.exit("Error: File must be a CSV file (.csv)")
    else:
        filename = sys.argv[1]
        pizza_data = read_pizza_csv(filename)
        print(tabulate(pizza_data, headers="firstrow", tablefmt="grid"))
