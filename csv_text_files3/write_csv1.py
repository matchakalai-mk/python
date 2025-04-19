import csv

with open('data.csv', mode='w') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Name', 'Age', 'City'])

    # Write some data rows
    csv_writer.writerow(['Alice', 30, 'New York'])
    csv_writer.writerow(['Bob', 25, 'Los Angeles'])
    csv_writer.writerow(['Charlie', 35, 'Chicago'])
