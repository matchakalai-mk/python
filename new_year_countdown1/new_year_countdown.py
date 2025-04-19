# This program calculates the time remaining until New Year's Day of 2026.

# Import the datetime class from the datetime module to work with dates and times
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Create a datetime object representing January 1st, 2026 at midnight (00:00:00)
new_year_day = datetime(2026, 1, 1)

# Calculate the time difference between New Year's Day 2026 and the current moment
# The result is a timedelta object representing the duration between these two dates
difference = new_year_day - now

# Print the time difference to the console
# Output will show days, hours, minutes, and seconds remaining until 2026
print(difference)