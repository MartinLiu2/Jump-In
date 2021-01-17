# Calendar in form of python dictionary

from datetime import timedelta, date

class Calendar:
  def __init__(self):
    self.start = date(2021, 1, 1)
    self.end = date(2021, 12, 31)
    self.cal = {}
  

  def getcal(self):
    def daterange(date1, date2):
      for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

    for dt in daterange(self.start, self.end):
      self.cal[dt] = []
  
  def printcal(self):
    print(self.cal)
  
  

  