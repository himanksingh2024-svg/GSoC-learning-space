import mesa

class MoneyAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def step(self):
        if self.wealth == 0:
            return
        other = self.random.choice(list(self.model.agents))
        if other is not self:
            other.wealth += 1
            self.wealth -= 1

class MoneyModel(mesa.Model):
    def __init__(self, n_agents=50):
        super().__init__()
        self.datacollector = mesa.DataCollector(
            model_reporters={"Total wealth": lambda m: sum(a.wealth for a in m.agents)},
            agent_reporters={"Wealth": "wealth"}
        )
        for _ in range(n_agents):
            MoneyAgent(self)

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("step")