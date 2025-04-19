import csv

with open('data2.csv', mode='w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Name', 'Age', 'City'])

    # Create a list of data rows where each row contains name, age and city
    data_rows = [
        ['Alice', 30, 'New York'],     # First person's details
        ['Bob', 25, 'Los Angeles'],    # Second person's details
        ['Charlie', 35, 'Chicago']     # Third person's details
    ]

    # Write multiple data rows at once
    csv_writer.writerows(data_rows)