import os
import sys
import json
from hero import Hero

filename = 'roster'

def get(path):
    global fileroot
    fileroot = path
    
    if os.path.isfile(__jsonpath()):
        return parsejson(__jsonpath())
    elif os.path.isfile(__txtpath()):
        return parsetxt(__txtpath())
    else:
        sys.exit("Roster data not found")
        
def __jsonpath():
    return fileroot + '\\' + filename + '.json'

def __txtpath():
    return fileroot + '\\' + filename + '.txt'

def parsejson(path):
    file = open(path, 'r')
    
    roster = []
    for obj in json.load(file):
        hero = Hero(obj['name'], obj['enabled'], obj['combatant'], obj['recruited'])
        roster.append(hero)
        # print(hero)
    
    return roster
        
def parsetxt(path):
    file = open(path, 'r')

    roster = []
    for line in file.readlines():
        hero = Hero(line.strip(), None, None, None)
        roster.append(hero)
        # print(hero)
    
    save(roster)
    return roster

def save(roster):
    file = open(__jsonpath(), "w")
    json.dump([vars(hero) for hero in roster], file, indent=4)