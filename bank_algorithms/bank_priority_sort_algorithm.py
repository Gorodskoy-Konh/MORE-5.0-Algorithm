from .bank_unit import BankUnit
from .bank_client import BankClient

def bank_priority_sort_algorithm(banks: list[BankUnit], client: BankClient):
    """
    Sort list of banks according to estimated total waiting time.

    Parameters:
        banks (list[BankUnit]): List of banks for sorting according estimated wait time.

    Returns:
            binary_sum (str): Binary string of the sum of a and b
    """
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