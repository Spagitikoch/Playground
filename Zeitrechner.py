# Zeitrechner

from datetime import datetime
import time

def TimeCurrent():
    current_hour = int(datetime.now().strftime("%H"))
    current_min = int(datetime.now().strftime("%M"))
    current_sec = int(datetime.now().strftime("%S"))

    return [current_hour,current_min,current_sec]

def TimeIn(time, unit = "minutes"):

    input_time = int(time)
    
    current_hour = int(datetime.now().strftime("%H"))
    current_min = int(datetime.now().strftime("%M"))
    current_sec = int(datetime.now().strftime("%S"))

    result = [current_hour,current_min,current_sec]

    if unit == "h":
        result[0] += input_time
    if unit == "s":
        input_time /= 60
    
    
    result[1] += round(input_time)

    print(f"inputtime = {input_time}")

    while not (result[1]<60):
        result[1] -= 60
        result[0] += 1
    if result[0] > 23:
        result[0] = result[0] % 24
    

    print(f"in {time} {unit} it will be {result}")

def TimeTil(end, start):
    # Magischer Syntax Error
    remaining_hours = int(end[0]) - int(start[0])
    remaining_mins = int(end[1])- int(start[1])
    remaining_secs = int(end[2])- int(start[2])
    remaining = [remaining_hours,remaining_mins,remaining_secs]
    print(remaining)

TimeTil([16,0,15],TimeCurrent)