class Workoutunit():
  def __init__(self, name, reps):
    self.name = name
    self.reps = reps
    self.completed = False
  
  def mark_complete(self):
    self.completed = True
  
  def check_status(self):
    return self.completed
  
  def printworkoutunit(self):
    print(self.name)
    print(self.reps)