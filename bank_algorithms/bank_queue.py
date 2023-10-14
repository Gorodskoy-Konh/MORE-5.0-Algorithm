from .bank_client import BankClient

class BankQueue:
    """
    Queue of clients that are waiting for their services.
    """
    def __init__(self, clients: list[BankClient]) -> None:
        """
        Create a bank queue object.

        Parameters
        ----------
            clients: list[BankClient]
                List of clients waiting in queue in order of queue (First in list is first in queue, last in list is last in queue).
        """
        self.clients = clients

    def search_for_first(self, products: list[str]) -> int:
        for i in range(len(self.clients)):
            if self.clients[i].desired_product in products:
                return i
        return None
    
    def remove_by_index(self, index: int) -> None:
        self.clients = self.clients[:index] + self.clients[index+1:]
    
    def pop_required_client(self, products: list[str]) -> BankClient:
        index = self.search_for_first(products)
        client = self.clients[index]
        self.remove_by_index(index)
        return client
    
    def get_desired_products(self) -> set[str]:
        products = set()
        for client in self.clients:
            products.add(client.desired_product)
        return products

    def is_empty(self) -> bool:
        return len(self.clients) == 0

    def __len__(self) -> int:
        return len(self.clients)
    
