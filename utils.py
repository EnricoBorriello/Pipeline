from datetime import datetime, timedelta

def find_date_range(date_list):
    """
    given a list of dates in the MM/DD/YYYY format, 
    find the earliest and the latest ones.
    """
    # Convert the dates to datetime objects
    date_objects = [datetime.strptime(date_str, "%m/%d/%Y") for date_str in date_list]
    # Find the earliest and latest datea using the min() and max functions
    earliest_date = min(date_objects)
    latest_date = max(date_objects)
    # Convert the dates back to the MM/DD/YYYY format
    earliest_date_str = earliest_date.strftime("%m/%d/%Y")
    latest_date_str = latest_date.strftime("%m/%d/%Y")
    return earliest_date_str, latest_date_str