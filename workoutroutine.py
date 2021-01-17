class Routine:
  def __init__(self):
    self.workoutlist = []
    self.date = []
    self.time = []
    self.status = False
    self.type = "self"
  
  def addworkout(self, workoutunit):
    self.workoutlist.append(workoutunit)
  
  def setdate(self, date):
    self.date.append(date)
  
  def settime(self, time):
    self.time.append(time)
  
  def check_status(self):
    for workout in self.workoutlist:
      if workout.check_status == False:
        return False
    else:
      return True
    
  def change_routine_type(self):
    self.type = "assigned"
  
  def convert_to_dict(self, username):
    names = []
    reps = []
    for unit in self.workout[list]:
      names.append(unit.name)
      reps.append(unit.reps)
    return_dict = {"username": username, "names": names, "reps": reps}
    return return_dict

