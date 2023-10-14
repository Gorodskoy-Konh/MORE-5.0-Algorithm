from .bank_queue import BankQueue
from .bank_terminal import BankTerminal

class BankUnit:
    """
    Class for bank facilities
    """

    def __init__(self, bank_id: int, queue: BankQueue, terminals: list[BankTerminal], move_time: float) -> None:
        """
        Create a bank unit object.

        Parameters
        ----------
            bank_id: int
                The id of bank.
            queue: BankQueue
                Queue in the bank.
            terminals: list[BankTerminal]
                Terminals in the bank.
            move_time: float
                Time to move to this bank for the user-client.
            
        """
        self.bank_id = bank_id
        self.queue = queue
        self.move_time = move_time
        self.terminals = terminals


    def simulate_queue(self) -> float:
        full_passed_time = 0.0

        while not self.queue.is_empty():
            terminal = self.get_free_terminal(self.queue.get_desired_products())
            if terminal is None:
                min_wait_terminal = self.get_min_wait_terminal()
                passed_time = min_wait_terminal.wait_for_client()
                full_passed_time += passed_time
                for c_terminal in self.terminals:
                    if c_terminal.terminal_id != min_wait_terminal.terminal_id:
                        c_terminal.wait_some_time(passed_time)
                continue
                
            client = self.queue.pop_required_client(terminal.supported_services)
            terminal.attach_client(client)
            client.set_wait_time(full_passed_time)
    
    def get_free_terminal(self, products: set[str]) -> BankTerminal:
        for terminal in self.terminals:
            if terminal.is_free() and len(set(terminal.supported_services).intersection(products)) > 0:
                return terminal
        return None
    
    def get_min_wait_terminal(self) -> BankTerminal:
        min_terminal = self.terminals[0]
        for terminal in self.terminals:
            if terminal.remain_wait_time < min_terminal.remain_wait_time and not terminal.is_free():
                min_terminal = terminal
        return min_terminal