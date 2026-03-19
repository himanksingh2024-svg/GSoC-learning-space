import mesa
import enum

class State(enum.IntEnum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2

class PersonAgent(mesa.Agent):
    def __init__(self, model, state=State.SUSCEPTIBLE):
        super().__init__(model)
        self.state = state

    def step(self):
        if self.state == State.INFECTED:
            others = self.model.agents.select(lambda a: a.state == State.SUSCEPTIBLE)
            for other in self.random.sample(list(others), min(3, len(others))):
                if self.random.random() < self.model.infection_rate:
                    other.state = State.INFECTED
            if self.random.random() < self.model.recovery_rate:
                self.state = State.RECOVERED

class SIRModel(mesa.Model):
    def __init__(self, n_agents=100, infection_rate=0.3, recovery_rate=0.1):
        super().__init__()
        self.infection_rate = infection_rate
        self.recovery_rate = recovery_rate
        self.datacollector = mesa.DataCollector({
            "Susceptible": lambda m: sum(1 for a in m.agents if a.state == State.SUSCEPTIBLE),
            "Infected": lambda m: sum(1 for a in m.agents if a.state == State.INFECTED),
            "Recovered": lambda m: sum(1 for a in m.agents if a.state == State.RECOVERED),
        })
        for i in range(n_agents):
            state = State.INFECTED if i < 5 else State.SUSCEPTIBLE
            PersonAgent(self, state=state)

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("step")