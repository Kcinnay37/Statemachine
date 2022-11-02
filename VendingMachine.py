from transitions import Machine, State
from transitions.extensions import MachineFactory, GraphMachine

diagram_cls = MachineFactory.get_predefined(graph=True)

class VendingMachine(object):
    machine:Machine
    states = []
    maxCoins:int = 0
    currCoins:int = 0

    def __init__(self, maxCoins:int):
        self.maxCoins = maxCoins

        #peut rentrer les fontion enter et exit dans State dans les parametre du constru
        self.states.append(State("Idle"))
        self.states.append(State("EnoughCoins"))

        #diagram_cls est une machine avec plsu de trucs
        self.machine = diagram_cls(model=self, states=self.states, initial="Idle", show_auto_transitions=True, show_conditions=True, show_state_attributes=True)

        self.machine.add_transition("insert_coin", "Idle", "EnoughCoins", conditions=["has_enough_coins"])
        self.machine.add_transition("insert_coin", "Idle", "Idle")

        self.machine.add_transition("dispense_product", "EnoughCoins", "Idle")
        self.machine.add_transition("press_cancel", "EnoughCoins", "Idle")

    def insertCoin(self):
        self.currCoins += 1
        self.trigger("insert_coin")

    def dispense(self):
        self.currCoins = 0
        self.trigger("dispense_product")

    def has_enough_coins(self):
        return self.currCoins >= self.maxCoins
