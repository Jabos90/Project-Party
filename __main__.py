import os
import Roster
import Menu

if __name__ == '__main__':
    roster = Roster.get(os.path.dirname(__file__))
    Menu.start(roster)