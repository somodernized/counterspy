from random import randint

num_days = 3
move_prob = .1
agent_names = ["James Bond", "Kate Archer", "Sven Persson", "George Costanza", "Lorelai Gilmore", "Chuck Bartowski", "Mata Hari"]
location_names = ["London", "Paris", "Berlin", "Hong Kong"]

agents = []
exposed_agents = []
locations = []

class Agent:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.level = 0
        #location.agents.append(self)
    
    def move_to(self, target_location):
        if target_location is not self.location:
            self.location.agents.remove(self)
            self.location = target_location
            target_location.agents.append(self)
    
    def expose(self):
        print "%s was exposed in %s" % (self.name, self.location.name)
        self.location.agents.remove(self)
        self.location = None
        agents.remove(self)
        exposed_agents.append(self)
    
class Location:
    
    def __init__(self, name):
        self.name = name
        self.agents = []
    
    def fight(self):
        print "There's a fight in %s between %s" % (self.name, comma_list(names_of(self.agents)))
        loser = self.agents[randint(0, len(self.agents) - 1)]
        loser.expose()

def comma_list(str_list):
    length = len(str_list)
    if length > 2:
        str_list[-1] = "and " + str_list[-1]
        return ", ".join(str_list)
    elif length > 0:
        return " and ".join(str_list)
    else:
        return "none"

def names_of(obj_list):
    return [obj.name for obj in obj_list]

def random_from(obj_list):
    return obj_list[randint(0, len(obj_list) - 1)]

def initialize_locations(names):
    return [Location(name) for name in names]

def initialize_agents(names):
    agents = []
    for name in names:
        l = random_from(locations)
        a = Agent(name, l)
        agents.append(a)
        l.agents.append(a)
    return agents

def update():
    num_agents = len(agents)
    for a in agents:
        if randint(0, 10) / 10. <= move_prob:
            a.move_to(random_from(locations))
            print "%s moves to %s" % (a.name, a.location.name)
    
    for l in locations:
        if len(l.agents) > 1:
            l.fight()

if __name__ == "__main__":
    locations = initialize_locations(location_names)
    agents = initialize_agents(agent_names)
    
    for t in range(0, num_days):
        print "Day %d" % (t)
        update()
        print
    
    print "Active Agents"
    print comma_list(names_of(agents))
    print "Exposed Agents"
    print comma_list(names_of(exposed_agents))