import csv
import sys

def scourgify(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in reader:
                last, first = row['name'].split(', ')
                writer.writerow({'first': first, 'last': last, 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Error: {input_file} does not exist.")
    except Exception as e:
        sys.exit(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        scourgify(input_file, output_file)
