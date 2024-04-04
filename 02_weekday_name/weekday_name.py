def weekday_name(day_of_week):
    DayNames= ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    if day_of_week < 1 or day_of_week > 7:
        return None
    return DayNames[day_of_week-1]




    
print(weekday_name(1))

print(weekday_name(7))
        
print(weekday_name(9))

print(weekday_name(0))
