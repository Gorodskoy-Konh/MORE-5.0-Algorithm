from .bank_client import BankClient

class BankTerminal:
    """
    Class that represents terminal in bank.
    """
    def __init__(self, terminal_id : int, service_avg_times: dict[str, float]) -> None:
        """
        Create a bank terminal object.

        Parameters
        ----------
            terminal_id: int
                The id of a terminal.
            service_avg_times: dict[str, float]
                Dictionary where key is name of service and value is average execution time for this service.
        """
        
        self.supported_services = list(service_avg_times.keys())
        self.service_avg_times = service_avg_times
        self.terminal_id = terminal_id
        self.client = None
        self.remain_wait_time = 0.0

    def attach_client(self, client: BankClient):
        if not client.desired_product in self.supported_services:
            raise Exception("This client cannot be attached here!")
        self.client = client
        self.remain_wait_time = self.service_avg_times[client.desired_product]

    def is_free(self):
        return self.client == None
    
    def wait_for_client(self):
        passed_time = self.remain_wait_time
        self.client = None
        return passed_time
    
    def wait_some_time(self, passed_time: float):
        self.remain_wait_time -= passed_time
        if self.remain_wait_time < 0:
            self.remain_wait_time = 0.0
            self.client = None