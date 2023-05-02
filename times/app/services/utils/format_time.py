def format_time(time_str):
    if ":" in time_str:
        minutes, seconds = time_str.split(":")
        time = int(minutes) * 60 + float(seconds)
    else:
        time = float(time_str)
    return time