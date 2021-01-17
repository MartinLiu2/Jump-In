# overarching class that defines a new user
from profile import Profile
from forum import Forum
from workout import Workout

class User:
  def __init__(self, name, country, sex):
    self.name = name
    self.country = country
    self.sex = sex
    self.authentication = "XXX"
    self.team = []
    self.group = []

    #creating profiles for each user
    self.profile = Profile(self.name, self.sex)

    

    