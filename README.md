# Алгоритм подбора банков
## Описание
Алгоритм находит лучшие банки и оценочное время ожидания для конкретного пользователя среди списка банков, учитывая очереди в этих банках, среднее время выполнения услуг и время дороги до этих банков.
### Упрощённое объяснение работы алгоритма
1. Симулировать очереди внутри банков и получает время ожидания в этих очередях для пользователя если он будет последним.
2. Вычислить оценочное время ожидания учитывая время дороги до банка и время ожидания в очереди банка в момент прибытия пользователя в банк
3. Остортировать все банки по оценочному времени ожидания
## Использование
### Создание банков
Чтобы создать банк нужно иметь список терминалов в этом банке и текущую очередь клиентов.
#### Создание терминала
```python
from bank_algorithms.bank_terminal import BankTerminal

# Услуги доступные в терминали для выполнения
supported_services = {
    "Кредиты": 780.0, # Название услуги : среднее время обслуживание этой услуги (секунды)
    "Ипотека": 420.0
}

# ID терминала
terminal_id = 0


terminal = BankTerminal(terminal_id, supported_services)
```

#### Создание очереди клиентов
```python
from bank_algorithms.bank_client import BankClient
from bank_algorithms.bank_queue import BankQueue

# Список клиентов в порядке очереди (самый первый - первый в очереди)
clients = [
    BankClient("Кредиты"),
    BankClient("Ипотека"), # Объект клиента, для создания нужна услуга, которую он хочет
    BankClient("Кредиты"),
]

queue = BankQueue(clients)
```
Теперь когда всё есть можно инициализировать банк.
```python
from bank_algorithms.bank_unit import BankUnit

terminals = [BankTerminal(...), BankTerminal(...), ...] # Список терминалов, создание описано выше
queue = ... # Очередь пользователей в банк. Создание описано выше
bank_id = 0 # ID банка
move_time = 10000.0 # Время затрачиваемое на дорогу до банка (секунды).
bank = BankUnit(bank_id, queue, terminals, move_time)
```
### Использование алгоритма
```python
from bank_algorithms.bank_priority_sort_algorithm import bank_priority_sort_algorithm

banks = [BankUnit(...), BankUnit(...), ...]
user = BankClient("Ипотека") # Создание клиента банка на основе услуги которая нужна пользователю.

# Получаем список ID банков и оценочное время ожидания
best_banks_estimated, best_banks_move = bank_priority_sort_algorithm(banks, user)

best_bank_id, estimated_time = best_banks_estimated[0]
print(best_bank_id, estimated_time) # Вывести ID лучшего банка и лучшее время ожидания.

# Тоже самое и для 'best_bank_move', но отсортированно только по времени дороги до банка!!!
```