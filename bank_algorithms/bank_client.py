class BankClient:
    """
    Class to store desired products of a some client.
    """
    def __init__(self, desired_product: str) -> None:
        """
        Create a bank client object.

        Parameters
        ----------
            desired_product: str
                Product that client wants. 
        """
        self.desired_product = desired_product
        self.wait_time = -1.0
    
    def set_wait_time(self, wait_time: float):
        self.wait_time = wait_time
