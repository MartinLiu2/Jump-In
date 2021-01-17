#class returns the daily goal routine that are precoded (provided by us)
#user can create own workout in the workout class
from workoutunit import Workoutunit
from workoutroutine import Routine

class DailyGoal():
  def __init__(self, name):
    self.name = name
  
  def get_easy_goal(self):
    easygoal = Routine()
    jumpingjacks = Workoutunit("jumping jacks", 25)
    burpees = Workoutunit("Burpees", 25)
    pushups = Workoutunit("Push up", 25)
    deadlifts = Workoutunit("Deadlifts", 25)

    easygoal.addworkout(jumpingjacks)
    easygoal.addworkout(burpees)
    easygoal.addworkout(pushups)
    easygoal.addworkout(deadlifts)

    return easygoal.workoutlist
    
  
  def get_medium_goal(self):
    medgoal = Routine()
    jumpingjacks = Workoutunit("jumping jacks", 50)
    burpees = Workoutunit("Burpees", 50)
    pushups = Workoutunit("Push up", 50)
    deadlifts = Workoutunit("Deadlifts", 50)

    medgoal.addworkout(jumpingjacks)
    medgoal.addworkout(burpees)
    medgoal.addworkout(pushups)
    medgoal.addworkout(deadlifts)
    
    return medgoal.workoutlist
  
  def get_hard_goal(self):
    hardgoal = Routine()
    jumpingjacks = Workoutunit("jumping jacks", 75)
    burpees = Workoutunit("Burpees", 75)
    pushups = Workoutunit("Push up", 75)
    deadlifts = Workoutunit("Deadlifts", 75)

    hardgoal.addworkout(jumpingjacks)
    hardgoal.addworkout(burpees)
    hardgoal.addworkout(pushups)
    hardgoal.addworkout(deadlifts)
    
    return hardgoal.workoutlist