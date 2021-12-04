class Hero(object):
    def __init__(self, name, enabled, combatant, recruited):
        self.name = name
        self.enabled = enabled or True
        self.combatant = combatant or True
        self.recruited = recruited or False

    def __contains__(self, item):
        return item.lower() in self.name.lower()
        
    def __str__(self):
        return f"{self.name:<20} (Recruited: {self.recruited!s:>5}, Combatant: {self.combatant!s:>5})"
    
    def __repr__(self):
        return ' '.join(self.__str__().split())