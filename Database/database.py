import pymongo
from pymongo import MongoClient
import random


cluster = MongoClient("mongodb+srv://developer:sbhack@prototype.ccbwg.mongodb.net/test?retryWrites=true&w=majority")
MDB = cluster["MDB"]


def adduser(name, sex, age, country, username, password, bio):
  error01 = "Username already in use"
  collection = MDB['users']
  username_list = [user["username"] for user in collection]
  if username in username_list:
    return error01
  else:
    user = {"name": name, "sex": sex, "age": age, "country": country, "username": username, "password": password, "bio": bio}
    collection.insert_one(user)

def finduser(input):
  collection = MDB['users']
  for user in collection.find():
    if user['username'] == input or user['name'] == input:
      return user

def creategroup(group_name, description, requirements, username):
  collection = MDB['groups']
  id_list = [group["groupid"] for group in collection.find()]
  rand = random.randrange(100000,999999,1)
  while rand in id_list:
    rand = random.randrange(100000,999999,1)
  group = {"_id":rand, "name": group_name, "description": description, "requirements": requirements, "members":[username]}
  collection.insert_one(group)
    

def findgroup(input):
  collection = MDB['groups']
  for group in collection.find():
    if str(group["name"]) == str(input) or int(group["groupid"]) == int(input):
      return group
    

def createteam(name, school, association, sport, description, username):
  collection = MDB['teams']
  id_list = [group["groupid"] for group in collection.find()]
  rand = random.randrange(100000,999999,1)
  while rand in id_list:
    rand = random.randrange(100000,999999,1)
  team = {"_id": rand, "name": name, "school":school, "association":association, "sport":sport, "description":description, "members": [username], "teamid": rand}
  collection.insert_one(team)


def findteam(input):
  collection = MDB['team']
  for group in collection.find():
    if str(group["name"]) == str(input) or int(group["groupid"]) == int(input):
      return group

def leaderboard(username, daily, weekly):
  #access database see if username exists
  collection = MDB['leaderboard']
  flag = False
  for user in collection.find():
    if username == user["username"]:
      flag = True
    if flag:
      new_value = {"$set" : {"username": username, "daily_score": daily, "weekly_score": weekly}}
      collection.update_many(user, new_value)
  #if exists, update score
  if not flag:
    leaderboard_user = {"username": username, "daily_score": daily, "weekly_score": weekly}
    collection.insert_one(leaderboard_user)

  #rank the DB in order of most points to least
  dailyrank = []
  for user in collection.sort("daily_score", -1)
    dailyrank.append(user)
  for i in dailyrank:
    if dailyrank[i]["username"] == username:
      day_rank = i + 1
      day_score = dailyrank[i]["daily_score"]
      break
  
  weeklyrank = []
  for user in collection.sort("weekly_score", -1)
    weeklyrank.append(user)
  for i in weeklyrank:
    if weeklyrank[i]["username"] == username:
      week_rank = i + 1
      week_score = weeklyrank[i]["weekly_score"]
      break
    
  #find the rank of the username and return the rank
  return day_rank, day_score, week_rank, week_score

def user_2factorauthentication(username):
  collecection = MDB['authentication']
  flag = True
  while flag:
    auth_key = random.randrange(100000,999999,1)
    for active_auth_factor in collection.find():
      if auth_key in active_auth_factor.keys():
        flag = True
    else:
      flag = False
  post = {auth_key:username}
  collection.insert_one(post)

def alexa_2factorauthentication(key):
  error = "key not found"
  collection = MDB['authentication']
  if collection.get(key) != None:
    username = collection[key]
    return username
    #if successful delete the key value pair
  else:
    return error
  
  
  
def add_routine(routine):
  collection = MDB("WOR")
  collection.insert_one(routine)


def get_routine():
  collection = MDB("WOR")
  tuple_list = []
  for routine in collection:
    workout_names = routine["names"]
    reps = routine["reps"]
    for i in range(len(workout_names)):
      tuple_list.append((workout_names[i], reps[i]))
    return(tuple_list)
