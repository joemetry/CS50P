import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Updated pattern to capture hours without minutes and with optional spaces around 'to'
    pattern = r'^(1[0-2]|0?[1-9])(?::([0-5][0-9]))?\s(AM|PM)\s?to\s?(1[0-2]|0?[1-9])(?::([0-5][0-9]))?\s(AM|PM)$'
    match = re.match(pattern, s)
    if match:
        start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
        start_minute = start_minute if start_minute else '00'
        end_minute = end_minute if end_minute else '00'
        start_hour = convert_to_24_hour(int(start_hour), start_period)
        end_hour = convert_to_24_hour(int(end_hour), end_period)
        return f'{start_hour}:{start_minute} to {end_hour}:{end_minute}'
    raise ValueError("Invalid time format")

def convert_to_24_hour(hour, period):
    if period == 'AM' and hour == 12:
        return '00'
    elif period == 'PM' and hour != 12:
        return f'{hour + 12}'
    return f'{hour:02}'

if __name__ == "__main__":
    main()
