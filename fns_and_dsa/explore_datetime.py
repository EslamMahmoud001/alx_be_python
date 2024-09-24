from datetime import date, timedelta, datetime

def display_current_datetime():
    """ A function to display current date and time. """
    current_date = datetime.now()
    return print(f"Current date and time: {current_date}")


def calculate_future_date():
    """ A function to calculate future date. """
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = date.today() + timedelta(days = number_of_days)
    
    return print(f"Future date: {future_date}")
