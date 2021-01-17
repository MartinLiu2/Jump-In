from workout import Workout
from datetime import datetime
from calendar import calendar
from datetime import timedelta, date

class Profile():
  def __init__(self, username, sex):
    self.username = username
    self.bio = [] 
    self.sex = sex
    self.hydration = 0
    self.hydration_goal = 0
    self.workout = Workout(self.name)
    

    current = datetime.date(datetime.now())
    split = current.split('-')
    int_date = split[1] * 100 + split[2]
    self.date = int_date

    
  def edit_bio(self, newbio):
    self.bio.clear()
    self.bio.append(newbio)

  # HYDRATION METER

  def add_hydration(self, hydration):
    #add "hydration" to the current amount of water drank
    if (self.sex == "male"):
      self.hydration_goal = 3.7 #in liters
    elif (self.sex == "female"):
      self.hydration_goal = 2.7 #in liters
      
    self.hyrdation += hydration

  def hydration_goal(self):
    #checks if the hydration goal is met# Check if hydration goal reached
    if self.hydration >= self.hydration_goal:
      return True
    else:
      return False
    
  def hydration_percentage(self):
    percent = self.hydration/self.hydration_goal
    return percent

  #CALENDAER/ Time component

  def reset_day(self):
    current = datetime.date(datetime.now())
    split = current.split('-')
    int_date = split[1] * 100 + split[2]
    if int_date != self.date:
      self.workout.reset_daily_goal()
      self.date = int_date
    
  def find_active_streak(self):
    current_date = datetime.now()
    Completed = True
    temp_date = current_date - timedelta(1)
    c = 0
    while (Completed):
      Completed = self.workout.calendar.cal[temp_date].check_status()
      c += 1
    return c

    