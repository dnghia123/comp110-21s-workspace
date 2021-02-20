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


Population:int = int(input("Population:"))
Doses_administered:int = int(input("Doses administered:")) 
Doses_per_day:int = int(input("Doses per day:"))
Target_percent_vaccinated: float = int(input("Target percent vaccinated:")) 
today: datetime = datetime.today()
Doses_target_goal:float = ((Target_percent_vaccinated/100) * Population) - (Doses_administered/2) 
Days_till_target_goal: float = (Doses_target_goal * 2) / (Doses_per_day)  
Days_till_goal: timedelta =timedelta(Days_till_target_goal)
Date_of_goal: datetime = today + Days_till_goal 
print("We will reach " + str(Target_percent_vaccinated) + "% vaccination in " + str(Days_till_goal) + " which falls on " + str(Date_of_goal.strftime("%B %d, %Y")))    