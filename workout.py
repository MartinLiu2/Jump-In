from workoutunit import Workoutunit
from dailygoal import DailyGoal
import database
from calendar import Calendar
from datetime import timedelta, date
from datetime import datetime


class Workout():
  def __init__(self, username):
    self.username = username
    self.workout_list = []
    self.subscribed_list = []
    self.completed_list = []
    self.dailygoal = DailyGoal("dailygoal")
    self.calendar = Calendar()
    self.calendar.getcal()

  def add_workout(self, name, date, time, reps):
    new_workout = Workoutunit(name, date, time, reps)
    self.workout_list.append(new_workout)
    
  def mark_completed(self, workout):
    workout.completed = True
    self.completed_list.append(workout)
    self.workout_list.remove(workout)
  
  def check_workouts(self):
    return self.workout_list
  
  def check_completed(self):
    return self.completed_list

  # GOALS 

  def set_daily_goals(self, difficulty):
    current = datetime.date(datetime.now())

    if difficulty == "easy":
      daily_goal = self.dailygoal.get_easy_goal()
      daily_goal_dict = daily_goal.convert_to_dict(self.username)
      database.add_routine(daily_goal_dict)
      self.workout_list.append(daily_goal)
      self.calendar.cal[current].append(daily_goal)
    elif difficulty == "intermediate":
      daily_goal = self.dailygoal.get_med_goal()
      daily_goal_dict = daily_goal.convert_to_dict(self.username)
      database.add_routine(daily_goal_dict)
      self.workout_list.append(daily_goal)
      self.calendar.cal[current].append(daily_goal)
    elif difficulty == "hard":
      daily_goal = self.dailygoal.get_hard_goal()
      daily_goal_dict = daily_goal.convert_to_dict(self.username)
      database.add_routine(daily_goal_dict)
      self.workout_list.append(daily_goal)
      self.calendar.cal[current].append(daily_goal)

  def daily_goal_status(self, routine):
    for workoutunit in routine:
      if workoutunit.status == False:
        return False
    else:
      return True

  def reset_daily_goal(self, daily_goal):
    for workout_routine in self.workout_list:
      if workout_routine.name == "dailygoal":
        self.workout_list.remove(workout_routine)

#Assign Workouts

  def assign_workout(self, routine, date):
    routine.change_routine_type()
    self.calendar.cal[date].append(routine)
  
  def friendly_workout(self, routine, date):
    self.calendar.cal[date].append(routine)

#Leaderboard statistics

  def get_daily_score(self):
    count = 0
    current = datetime.now()
    all_routine = self.calendar.cal.get(current)
    for routine in all_routine:
      if routine.checkstatus:
        count += 1
    
  
  def get_weekly_score(self):
    count = 0
    current = datetime.now()
    for i in range(1, 7):
      for routine in self.calendar.cal[current-timedelta(i)]:
        if routine.check_status():
          count += 1
    return count
        

        
  
