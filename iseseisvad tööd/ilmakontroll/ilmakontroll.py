from day_control import day_control
from month_control import month_control
from weather_control import weather_control

day = day_control()
month = month_control()
weather = weather_control()
print(f"Tänane päev on {day} ja praegune kuu on {month} ja ilm on {weather}")