import twint
from datetime import datetime
current_time=datetime.today()
import os
from pathlib import Path
path=os.path.join(Path(__file__).resolve().parent.parent,"generated")

day=current_time.day
month=current_time.month
year=current_time.year
hour=current_time.hour
minute=current_time.minute
second=current_time.second


def csv_creator_two(search):
    c = twint.Config()
    c.Search= search
    c.Limit = 200
    c.Store_csv = True
    c.Output = f"output_{day}_{month}_{year}_{hour}_{minute}.csv"
    
    twint.run.Search(c)
