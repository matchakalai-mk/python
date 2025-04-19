import csv

# Open the CSV file in read mode
with open('jokes_csv.csv', mode='r') as csv_file:

    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    next(csv_reader)  

    # Iterate through each row in the CSV file
    for row in csv_reader:

        joke = row[1]  # Assuming the joke is in the second column (index 1)
        rating = row[2]  # Assuming the rating is in the third column (index 2)

        # Print each joke and its rating
        print(f"Joke: {joke}, Rating: {rating}")