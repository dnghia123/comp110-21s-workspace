"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta
from exercises.ex01.vaccine_calc import Days_till_target_goal

__author__ = "730410603"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population,doses,doses_per_day,target)
    date: str = future_date(days)
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " which falls on " + str(date)) 


def days_to_target(population:int,doses:int,doses_per_day:int,target:int) -> int:
    """Days until target is reached"""
    Doses_target_goal:int = int(((target/100) * population) - (doses/2)) 
    Days_till_target_goal: int = int((Doses_target_goal * 2) / (doses_per_day)) 
    return Days_till_target_goal 


def future_date(days:int) -> str: 
    """Date of target"""
    Days_till_goal: timedelta =timedelta(days)
    today: datetime = datetime.today()
    Date_of_goal: datetime = today + Days_till_goal 
    return Date_of_goal.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
