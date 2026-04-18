#Read CSV file, transform data, and write to new CSV file
import csv

def transform(row):
    row["name"] = row["name"].upper()
    row["age"] = int(row["age"])
    return row

with open("input.csv") as infile, open("output.csv", "w") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        writer.writerow(transform(row))