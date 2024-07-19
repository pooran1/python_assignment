
# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".
from datetime import date

def print_current_date():
    today = date.today()
    print(today.strftime("%Y-%m-%d"))

print_current_date()
# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

from datetime import datetime

def convert_date_format(date_str):
    # Parse the input date string to a datetime object
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    
    # Convert the datetime object to the desired format
    formatted_date = date_obj.strftime("%Y-%m-%d")
    
    return formatted_date

# Example usage
input_date = "07/19/2024"
output_date = convert_date_format(input_date)
print(output_date)

# Write a program that takes a birth year as input and calculates the age of a person.
from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Example usage
birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("Your age is: " + str(age))
# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input
from datetime import datetime

def days_until_next_birthday(birth_date):
    today = datetime.today()
    current_year_birthday = datetime(today.year, birth_date.month, birth_date.day)

    if current_year_birthday < today:
        next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
    else:
        next_birthday = current_year_birthday

    days_remaining = (next_birthday - today).days
    return days_remaining

# Example usage
birth_date_str = input("Enter your birth date (MM/DD/YYYY): ")
birth_date = datetime.strptime(birth_date_str, "%m/%d/%Y")

days_remaining = days_until_next_birthday(birth_date)
print("Days remaining until your next birthday: " + str(days_remaining))


# Write a program that calculates and displays the number of days between two given dates.
from datetime import datetime

def days_between_dates(date1_str, date2_str):
    # Convert strings to datetime objects
    date1 = datetime.strptime(date1_str, "%m/%d/%Y")
    date2 = datetime.strptime(date2_str, "%m/%d/%Y")
    
    # Calculate the difference in days
    difference = abs((date2 - date1).days)
    return difference

# Example usage
date1_str = input("Enter the first date (MM/DD/YYYY): ")
date2_str = input("Enter the second date (MM/DD/YYYY): ")

days_difference = days_between_dates(date1_str, date2_str)
print("Number of days between the two dates: " + str(days_difference))
# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).
from datetime import datetime

def get_day_of_week(date_str):
    # Convert the string to a datetime object
    date = datetime.strptime(date_str, "%m/%d/%Y")
    # Get the day of the week
    day_of_week = date.strftime("%A")
    return day_of_week

# Example usage
date_str = input("Enter the date (MM/DD/YYYY): ")
day_of_week = get_day_of_week(date_str)
print("The day of the week is: " + day_of_week)
# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module
def is_leap_year(year):
    """Return True if year is a leap year, else False."""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def get_days_in_month(year, month):
    """Return the number of days in the given month of the given year."""
    if month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    elif month == 2:  # February
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31  # January, March, May, July, August, October, December

# Example usage
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Validate the month input
if 1 <= month <= 12:
    days = get_days_in_month(year, month)
    print(f"There are {days} days in month {month} of the year {year}.")
else:
    print("Invalid month. Please enter a month between 1 and 12.")

# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.
from datetime import datetime, timedelta

def calculate_future_date(start_date_str, days):
    """
    Calculate the date that is a specified number of days in the future.

    :param start_date_str: Start date in the format "YYYY-MM-DD"
    :param days: Number of days to add
    :return: None
    """
    # Convert the start date string to a datetime object
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    # Add the specified number of days to the start date
    future_date = start_date + timedelta(days=days)
    
    # Print the future date
    print(f"The date {days} days after {start_date_str} is {future_date.strftime('%Y-%m-%d')}.")

# Example usage
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
days = int(input("Enter the number of days: "))

calculate_future_date(start_date_str, days)

# Write a Python program that uses the datetime module to print the current date and time.
from datetime import datetime

# Get the current date and time
current_date_time = datetime.now()

# Print the current date and time
print("Current date and time:", current_date_time)

from datetime import datetime

# Get the current date and time
current_date_time = datetime.now()

# Format the current date and time
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted current date and time
print("Current date and time:", formatted_date_time)

# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".
from datetime import datetime

def reformat_datetime(date_str):
    # Define the input and output formats
    input_format = "%m/%d/%Y %H:%M:%S"
    output_format = "%Y-%m-%d %H:%M:%S"
    
    # Parse the input datetime string
    try:
        parsed_datetime = datetime.strptime(date_str, input_format)
        
        # Format the datetime to the desired format
        formatted_datetime = parsed_datetime.strftime(output_format)
        
        return formatted_datetime
    except ValueError as e:
        return f"Error: {e}"

# Example usage
input_date_str = "07/19/2024 15:30:00"
formatted_date_str = reformat_datetime(input_date_str)
print("Formatted datetime:", formatted_date_str)

# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.
from datetime import datetime

def calculate_time_difference(start_str, end_str):
    # Define the datetime format
    datetime_format = "%Y-%m-%d %H:%M:%S"
    
    try:
        # Parse the input datetime strings
        start_datetime = datetime.strptime(start_str, datetime_format)
        end_datetime = datetime.strptime(end_str, datetime_format)
        
        # Calculate the time difference
        time_difference = end_datetime - start_datetime
        
        # Extract hours, minutes, and seconds from the time difference
        total_seconds = time_difference.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        
        return f"Time difference is {hours} hours, {minutes} minutes, and {seconds} seconds."
    except ValueError as e:
        return f"Error: {e}"

# Example usage
start_datetime_str = "2024-07-19 10:00:00"
end_datetime_str = "2024-07-19 14:35:45"
time_difference_str = calculate_time_difference(start_datetime_str, end_datetime_str)
print(time_difference_str)

# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.
from datetime import datetime, timedelta

def add_hours_to_datetime(original_datetime, hours_to_add):
    """
    Adds a specified number of hours to a given datetime object.
    
    :param original_datetime: The original datetime object.
    :param hours_to_add: The number of hours to add.
    :return: A new datetime object with the hours added.
    """
    # Create a timedelta object with the specified number of hours
    time_delta = timedelta(hours=hours_to_add)
    
    # Add the timedelta to the original datetime
    new_datetime = original_datetime + time_delta
    
    return new_datetime

# Example usage
original_datetime = datetime(2024, 7, 19, 10, 0, 0)
hours_to_add = 5
new_datetime = add_hours_to_datetime(original_datetime, hours_to_add)

print("Original datetime:", original_datetime)
print("New datetime after adding hours:", new_datetime)

# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().
from datetime import datetime

def format_datetime_as_month_day_year(dt):
    """
    Formats a datetime object as "Month Day, Year".
    
    :param dt: The datetime object to format.
    :return: The formatted date string.
    """
    # Format the datetime object as "Month Day, Year"
    formatted_date = dt.strftime("%B %d, %Y")
    
    return formatted_date

# Example usage
now = datetime.now()
formatted_date = format_datetime_as_month_day_year(now)

print("Formatted date:", formatted_date)

# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().
from datetime import datetime

def format_datetime_as_day_month_year(dt):
    """
    Formats a datetime object as "Day-Month-Year".
    
    :param dt: The datetime object to format.
    :return: The formatted date string.
    """
    # Format the datetime object as "Day-Month-Year"
    formatted_date = dt.strftime("%d-%B-%Y")
    
    return formatted_date

# Example usage
now = datetime.now()
formatted_date = format_datetime_as_day_month_year(now)

print("Formatted date:", formatted_date)

# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/
from datetime import datetime

# Define the date-time string
date_string = "26-08-2023 15:18:33.983780-07:00"

# Convert the date-time string to a datetime object
# First, replace the format to be compatible with the isoformat
iso_date_string = date_string.replace(' ', 'T')

# Parse the string into a datetime object
dt = datetime.fromisoformat(iso_date_string)

print("Datetime object:", dt)

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/
from datetime import datetime

# Define the date-time string
date_string = "08-26-2023 08:10:00 PM"

# Define the format of the input string
date_format = "%m-%d-%Y %I:%M:%S %p"

# Convert the date-time string to a datetime object
dt = datetime.strptime(date_string, date_format)

print("Datetime object:", dt)

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/
from datetime import datetime

# Define the date-time string
date_string = "08-26-2023 08:10:00 PM"

# Define the format of the input string
date_format = "%m-%d-%Y %I:%M:%S %p"

# Convert the date-time string to a datetime object
dt = datetime.strptime(date_string, date_format)

print("Datetime object:", dt)

# dt_named_and_short_form_format = "8-August-23 08:10:00"
# hint: https://strftime.org/
from datetime import datetime

# Define the date-time string
date_string = "8-August-23 08:10:00"

# Define the format of the input string
date_format = "%d-%B-%y %H:%M:%S"

# Convert the date-time string to a datetime object
dt = datetime.strptime(date_string, date_format)

print("Datetime object:", dt)

# create a current datetime and then displays it in the format "HH:MM AM/PM"
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the current time in "HH:MM AM/PM" format
formatted_time = now.strftime("%I:%M %p")

print("Current time:", formatted_time)

# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".
from datetime import datetime

def convert_date_format(date_str):
    # Parse the input date string
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    # Format the date object to the new format
    return date_obj.strftime("%Y-%m-%d")

# Get the date input from the user
user_date = input("Enter a date in MM/DD/YYYY format: ")
# Convert and print the date in YYYY-MM-DD format
print("Converted date:", convert_date_format(user_date))

# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/
from datetime import datetime

def get_day_of_week(date_obj):
    # Format the datetime object to display the day of the week
    return date_obj.strftime("%A")

# Example usage
now = datetime.now()  # Get the current datetime
print("Today is:", get_day_of_week(now))

# Create a function that takes a timezone name as input and prints the current date time object in that timezone.
from datetime import datetime
import pytz

def print_current_time_in_timezone(timezone_name):
    try:
        # Get the current datetime in UTC
        utc_now = datetime.now(pytz.utc)
        
        # Convert UTC datetime to the desired timezone
        timezone = pytz.timezone(timezone_name)
        local_time = utc_now.astimezone(timezone)
        
        # Print the datetime in the desired timezone
        print("Current date and time in", timezone_name, ":", local_time.strftime("%Y-%m-%d %H:%M:%S"))
    
    except pytz.UnknownTimeZoneError:
        print("Unknown timezone:", timezone_name)

# Example usage
print_current_time_in_timezone("America/New_York")
print_current_time_in_timezone("Asia/Tokyo")
print_current_time_in_timezone("Europe/London")
# Write a program that converts a given date time (tz aware) string from one timezone to another.
from datetime import datetime
import pytz

def convert_datetime_between_timezones(datetime_str, source_tz_name, target_tz_name, fmt="%Y-%m-%d %H:%M:%S"):
    try:
        # Define the format for parsing and formatting the datetime
        format_str = fmt
        
        # Parse the input datetime string assuming it's in the source timezone
        source_tz = pytz.timezone(source_tz_name)
        target_tz = pytz.timezone(target_tz_name)
        
        # Create a naive datetime object from the input string
        naive_datetime = datetime.strptime(datetime_str, format_str)
        
        # Localize the naive datetime to the source timezone
        source_datetime = source_tz.localize(naive_datetime)
        
        # Convert to the target timezone
        target_datetime = source_datetime.astimezone(target_tz)
        
        # Print the datetime in the target timezone
        print("Converted datetime in", target_tz_name, ":", target_datetime.strftime(format_str))
    
    except pytz.UnknownTimeZoneError:
        print("Unknown timezone:", source_tz_name, "or", target_tz_name)
    except ValueError as e:
        print("Error parsing date:", e)

# Example usage
convert_datetime_between_timezones("2024-07-19 12:00:00", "America/New_York", "Asia/Tokyo")
convert_datetime_between_timezones("2024-07-19 12:00:00", "Europe/London", "Australia/Sydney")

# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.
from datetime import datetime
import pytz

def localize_datetime(naive_datetime, timezone_name):
    try:
        # Define the timezone
        tz = pytz.timezone(timezone_name)
        
        # Localize the naive datetime
        localized_datetime = tz.localize(naive_datetime)
        
        return localized_datetime
    
    except pytz.UnknownTimeZoneError:
        print(f"Unknown timezone: {timezone_name}")
        return None

# Example usage
naive_datetime = datetime(2024, 7, 19, 15, 30)  # Naive datetime object
timezone_name = "America/New_York"

localized_datetime = localize_datetime(naive_datetime, timezone_name)
if localized_datetime:
    print("Localized datetime:", localized_datetime.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone
from datetime import datetime, timedelta
import pytz

def print_time_in_timezone(timezone_name, hours_to_add):
    try:
        # Define the timezone
        tz = pytz.timezone(timezone_name)
        
        # Get the current time in UTC and localize it
        current_time_utc = datetime.now(pytz.utc)
        
        # Convert the UTC time to the desired timezone
        current_time_local = current_time_utc.astimezone(tz)
        
        # Add the specified number of hours
        future_time = current_time_local + timedelta(hours=hours_to_add)
        
        # Print the result
        print("Current time in", timezone_name, ":", current_time_local.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
        print("Time after", hours_to_add, "hours in", timezone_name, ":", future_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    
    except pytz.UnknownTimeZoneError:
        print(f"Unknown timezone: {timezone_name}")

# Example usage
timezone_name = "America/New_York"
hours_to_add = 5

print_time_in_timezone(timezone_name, hours_to_add)

# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated
from datetime import datetime, timedelta
import pytz

def find_dst_start(year, timezone_name, start_date_str):
    # Define the timezone
    tz = pytz.timezone(timezone_name)
    
    # Parse the start date
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    
    # Localize the start date to the given timezone
    start_date_tz_aware = tz.localize(start_date)
    
    # Initialize a datetime object for the given year and timezone
    current_date = start_date_tz_aware
    
    # Iterate through months to find when DST starts
    while current_date.year == year:
        if bool(current_date.dst()):
            # DST is activated
            break
        # Move to the next day
        current_date += timedelta(days=1)
    
    if bool(current_date.dst()):
        print("DST start date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    else:
        print("DST did not start in the given year.")

# Example usage
year = 2022
timezone_name = "US/Pacific"
start_date_str = "2022-01-01 00:00:00"

find_dst_start(year, timezone_name, start_date_str)


# Write a program that calculates the date and time of the daylight saving end in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated
from datetime import datetime, timedelta
import pytz

def find_dst_end(year, timezone_name, start_date_str):
    # Define the timezone
    tz = pytz.timezone(timezone_name)
    
    # Parse the start date
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    
    # Localize the start date to the given timezone
    start_date_tz_aware = tz.localize(start_date)
    
    # Initialize a datetime object for the given year and timezone
    current_date = start_date_tz_aware
    
    # Iterate through days to find when DST ends
    while current_date.year == year:
        if not bool(current_date.dst()):
            # DST is not activated, meaning DST has ended
            break
        # Move to the next day
        current_date += timedelta(days=1)
    
    if not bool(current_date.dst()):
        print("DST end date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    else:
        print("DST did not end in the given year.")

# Example usage
year = 2022
timezone_name = "US/Pacific"
start_date_str = "2022-01-01 00:00:00"

find_dst_end(year, timezone_name, start_date_str)

# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time

from datetime import datetime
import pytz

def convert_meeting_time(meeting_time_str, base_timezone, target_timezones):
    # Parse the meeting time
    meeting_time = datetime.strptime(meeting_time_str, "%d %B %Y at %I %p")
    
    # Define the base timezone
    base_tz = pytz.timezone(base_timezone)
    
    # Localize the meeting time to the base timezone
    meeting_time_base_tz = base_tz.localize(meeting_time)
    
    # Convert the meeting time to other timezones and print
    for tz in target_timezones:
        target_tz = pytz.timezone(tz)
        meeting_time_target_tz = meeting_time_base_tz.astimezone(target_tz)
        print(f"Meeting time in {tz}: {meeting_time_target_tz.strftime('%d %B %Y at %I:%M %p %Z')}")

# Example usage
meeting_time_str = "30 August 2023 at 2 PM"
base_timezone = "Asia/Karachi"  # Pakistan timezone
target_timezones = [
    "Europe/London",  # UK timezone
    "America/New_York",  # US Eastern Time
    "Asia/Riyadh",  # Saudi Arabia timezone
    "Asia/Karachi"  # Pakistan timezone (same as base)
]

convert_meeting_time(meeting_time_str, base_timezone, target_timezones)

# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop




# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration
from datetime import datetime
import pytz

# Initialize booking storage
booking_storage = []

def is_slot_available(start_date, end_date):
    """Check if the slot is available."""
    for booking in booking_storage:
        if (start_date < booking["end_date"] and end_date > booking["start_date"]):
            return False
    return True

def add_booking(start_date, end_date):
    """Add the booking to the storage."""
    booking_storage.append({
        "start_date": start_date,
        "end_date": end_date
    })

def convert_to_utc(datetime_str, timezone_str):
    """Convert a datetime string to UTC."""
    local_tz = pytz.timezone(timezone_str)
    local_dt = local_tz.localize(datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S"))
    return local_dt.astimezone(pytz.utc)

# Main function to handle booking logic
def main():
    for _ in range(5):
        start_datetime_str = input("Enter start datetime (YYYY-MM-DD HH:MM:SS): ")
        end_datetime_str = input("Enter end datetime (YYYY-MM-DD HH:MM:SS): ")
        timezone_str = input("Enter timezone (e.g., 'Asia/Karachi'): ")

        start_date_utc = convert_to_utc(start_datetime_str, timezone_str)
        end_date_utc = convert_to_utc(end_datetime_str, timezone_str)

        if is_slot_available(start_date_utc, end_date_utc):
            add_booking(start_date_utc, end_date_utc)
            print("Booking confirmed.")
        else:
            print("Slot not available.")

# Directly calling main() function
main()
