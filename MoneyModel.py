from mesa import Agent, Model


class MoneyAgent(Agent):
    """an agent with fixed initial wealth"""
    def __init__(self, unique_ID, model):
        super().__init__(unique_ID, model)
        self.wealth = 1


class MoneyModel(Model):
    """a model with some number of agents"""
    def __init__(self, N):
        self.num_agents = N
        # create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)