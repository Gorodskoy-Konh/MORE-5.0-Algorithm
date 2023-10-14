class BankClient:
    def __init__(self, desired_product: str) -> None:
        self.desired_product = desired_product
        self.wait_time = -1.0
    
    def set_wait_time(self, wait_time: float):
        self.wait_time = wait_time
