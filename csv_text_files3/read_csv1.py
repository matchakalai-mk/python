# Import the csv module to work with CSV files
import csv  

# Open the CSV file in read mode
with open(file='jokes_csv.csv', mode='r') as csv_file:

    # Create a CSV reader object to read the file
    csv_reader = csv.reader(csv_file)

    # Iterate through each row in the CSV file and print the current row
    for row in csv_reader:  
        print(row)