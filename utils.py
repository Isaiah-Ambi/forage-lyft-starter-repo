from datetime import datetime

def calculate_years_difference(given_date):
    
    
    current_date = datetime.today().date()
    years_difference = current_date.year - given_date.year
    
    # Adjust if the current month and day are before the given date's month and day
    if (current_date.month, current_date.day) < (given_date.month, given_date.day):
        years_difference -= 1
    
    return years_difference

# Example Usage:
# given_date = datetime(1990, 1, 1).date()  # Replace this with your desired date
# difference_in_years = calculate_years_difference(given_date)
# print(f"Difference in years: {difference_in_years}")
