import sys
import random
import Roster

rand = ['randomize', 'random']
recr = ['recruit']
togg = ['toggle']
leav = ['exit']

def start(roster):
    print('Welcome to the deck of many heroes!')
    print()

    while(True):
        printmenu()
        userinput = queryInput()
        execute(roster, userinput)

def printmenu():
    print(rand[0].capitalize())
    print(recr[0].capitalize())
    print(togg[0].capitalize())
    print(leav[0].capitalize())
    print()

def queryInput():
    return input('> ')

def execute(roster, userinput):
    (command, args) = (userinput + ' ').split(' ', 1)
    command = command.lower()
    args = [arg.strip() for arg in args.split(',')]

    # print(f"Command: {command}, Arguments: {args}")

    updated = False
    for arg in args:
        if command in rand:
            randomize(roster, arg)
            print()
        elif command in recr:
            updated |= recruit(roster, arg)
        elif command in togg:
            updated |= toggle(roster, arg)
        elif command in leav:
            sys.exit()
        else:
            print(f"'{command}' is not a recognized command")
            break;

    if updated: Roster.save(roster)
    if command not in rand: print()

def randomize(roster, count):
    combatants = list(filter(lambda x: x.recruited and x.combatant and x.enabled, roster))
    if not combatants:
        print("No enabled combatants recruited")
        return;

    count = int(count) if count.isnumeric() else 5

    if len(combatants) <= count:
        selected = combatants
    else:
        random.shuffle(combatants)
        selected = list(combatants[:count])

    for hero in selected:
        print(f"\t{hero.name}")

def recruit(roster, name):    
    hero = findhero(roster, name)
    if not hero: return False
    if hero.recruited:
        print(f"You have already recruited '{hero.name}'")
        return False

    hero.recruited = True

    position = roster.index(hero)                                       # position in the complete roster
    position = sum(1 for h in roster[0:position] if not h.recruited)    # position in the deck

    print(f"{hero.name} recruited! ({position + 1})")
    return True

def toggle(roster, name):
    hero = findhero(roster, name)
    if not hero: return False
    
    hero.enabled = not hero.enabled
    print(f"{hero.name} { 'enabled' if hero.enabled else 'disabled'}!")
    return True

def findhero(roster, name):
    if not name:
        print("Please provide the name of a hero")
        return
    
    matches = list(filter(lambda x: name in x, roster))
    
    if not matches:
        print(f"Could not find any heroes whose name contains '{name}'")
        return
    elif len(matches) > 1:
        print(f"{len(matches)} matches for '{name}' found, please be more specific")
        return
    
    return matches[0]
    