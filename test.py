from bank_algorithms.bank_client import BankClient
from bank_algorithms.bank_terminal import BankTerminal
from bank_algorithms.bank_unit import BankUnit
from bank_algorithms.bank_queue import BankQueue
from bank_algorithms.bank_priority_sort_algorithm import bank_priority_sort_algorithm

moi_mujik = BankClient("B")

clients1 = [
    BankClient("A"),
    BankClient("A"),
    BankClient("B"), 
    BankClient("A"),
    BankClient("B"),
    BankClient("B"),
    BankClient("B"),
    BankClient("A"),
    BankClient("B"),
]

clients2 = [
    BankClient("A"),
    BankClient("A"),
    BankClient("B"), 
    BankClient("A"),
    BankClient("B"),
    BankClient("B"),
    BankClient("B"),
    BankClient("A"),
    BankClient("B"),
]

clients3 = [
    BankClient("C"),
    BankClient("C"),
    BankClient("C"), 
    BankClient("B"),
]

queue1 = BankQueue(clients1)
queue2 = BankQueue(clients2)
queue3 = BankQueue(clients3)

terminals1 = [
    BankTerminal(0, {"A": 2, "B": 1}),
    BankTerminal(1, {"B": 2, "A": 1}),
    BankTerminal(2, {"C": 0.5}),
]
terminals2 = [
    BankTerminal(0, {"A": 2}),
    BankTerminal(1, {"B": 3}),
    BankTerminal(2, {"C": 0.5}),
]

terminals3 = [
    BankTerminal(0, {"C": 1, "A": 2}),
    BankTerminal(1, {"B": 2, "A": 1})
]
bank1 = BankUnit(0, queue1, terminals1, 1)
bank2 = BankUnit(1, queue2, terminals2, 2)
bank3 = BankUnit(2, queue3, terminals3, 1)
print(bank_priority_sort_algorithm([bank1, bank2, bank3], moi_mujik, 0))