from datetime import datetime


def string_to_date(date_string):
    """Converts a date string in the format YYYY.MM.DD to a date object."""
    try:
        return datetime.strptime(date_string, "%Y.%m.%d").date()
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY.MM.DD")



def get_days_from_today(date_str: str):
    current_day = datetime.today().date()
    data_obj = string_to_date(date_str)
    return (current_day - data_obj).days

print(get_days_from_today("2025.01.01"))
