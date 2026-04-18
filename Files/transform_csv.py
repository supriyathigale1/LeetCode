# Read CSV file, transform data, and write to new CSV file
import csv

def transform(row):
    """
    Transform a CSV row by:
    - Converting name to uppercase
    - Converting age to integer
    """
    row["name"] = row["name"].upper()
    row["age"] = int(row["age"])
    return row

# Open input and output CSV files
with open("input.csv") as infile, open("output.csv", "w") as outfile:
    # Create CSV reader that returns dictionaries
    reader = csv.DictReader(infile)
    # Create CSV writer with same fieldnames as input
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

    # Write header row to output file
    writer.writeheader()

    # Process each row from input file
    for row in reader:
        # Transform the row and write to output file
        writer.writerow(transform(row))