from datetime import time, timedelta
from .bank_unit import BankUnit
from .bank_client import BankClient

def bank_priority_sort_algorithm(banks: list[BankUnit], client: BankClient, average_waiting_time: float):
    """
    Sort list of banks according to estimated total waiting time.
    Also sort by move times.

    Parameters:
        banks (list[BankUnit]): List of banks for sorting according estimated wait time.
        client (BankClient): Client for which we estimate waiting time.
        average_waiting_time (float): Average waiting time in queue in current time.

    Returns:
        estimate_times (list[tuple[int, float]]): List of tuples where first element is 'bank_id' and second is estimated waiting time.
        move_times (list[tuple[int, float]]): List of tuples where first element is 'bank_id' and second is move waiting time. 
    """
    estimate_times = []
    move_times = []
    for bank in banks:
        bank.queue.clients.append(client)
        bank.simulate_queue()
        
        if client.wait_time < bank.move_time:
            estimated_wait_time = bank.move_time + average_waiting_time
        else:
            estimated_wait_time = client.wait_time
        estimate_times.append((bank.bank_id, estimated_wait_time))
        move_times.append((bank.bank_id, bank.move_time))

    estimate_times.sort(key=lambda x: x[1])
    move_times.sort(key=lambda x: x[1])
    return estimate_times, move_times

def recorded_estimate_wait(record_time: time, averate_wait_time: float) -> time:
    """
    Add estimated time for a specific recording

    Parameters:
        record_time (datatime.time): Time of record.
        average_waiting_time (float): Average waiting time in queue in current time.

    Returns:
        estimate_time (float): Time user has to wait. 
    """
    record_timedelta = timedelta(hours=record_time.hour, minutes=record_time.minute, seconds=record_time.second)
    estimated_wait = averate_wait_time + record_timedelta.seconds
    return estimated_wait