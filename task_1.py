from datetime import datetime


def string_to_date(date_string):
    """Converts a date string in the format YYYY-MM-DD to a date object."""
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None



def get_days_from_today(date_str: str):
    date_obj = string_to_date(date_str)
    if date_obj is None:
        return 'Invalid date format. Expected [YYYY-MM-DD]'
    
    current_day = datetime.today().date()
    return (current_day - date_obj).days


