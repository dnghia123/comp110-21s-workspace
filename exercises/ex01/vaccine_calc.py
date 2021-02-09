"""A vaccination calculator."""

__author__ = "730410603"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


Population: int = 330000000
print("Population: 330000000")
Doses_administered: int = 32780860
print("Doses administered: 32780860")
Doses_per_day: int = 1319981
print("Doses per day: 1319981")
print("Target percent vaccinated: 80")
Target_population_vaccinated: float = (Population * 0.80) 
Time_until_target_percent: float = ((Target_population_vaccinated - Doses_administered)/Doses_per_day) 
Days_until_target_percent: timedelta = timedelta( Time_until_target_percent)
today: datetime = datetime.today() 
future: datetime = today + Days_until_target_percent
print("We will reach 80% vaccination in 176 days, which falls on August 03, 2021.")