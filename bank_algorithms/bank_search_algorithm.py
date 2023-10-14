from .bank_unit import BankUnit
from .bank_client import BankClient

def bank_search_algorithm(banks: list[BankUnit], client: BankClient):
    estimate_times = []
    for bank in banks:
        bank.queue.clients.append(client)
        bank.simulate_queue()
        
        if client.wait_time < bank.move_time:
            estimated_wait_time = bank.move_time
        else:
            estimated_wait_time = client.wait_time - bank.move_time
        estimate_times.append((bank.bank_id, estimated_wait_time))
    
    estimate_times.sort(key=lambda x: x[1])
    return estimate_times