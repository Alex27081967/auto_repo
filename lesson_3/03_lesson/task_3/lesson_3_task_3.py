from address import Address
from mailing import Mailing

# Создание адресов
to_addr = Address("123456", "Москва", "Тверская", "10", "25")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "5", "12")

# Создание почтового отправления
mail = Mailing(to_address=to_addr, from_address=from_addr, cost=350, track="TRACK123456")

# Печать информации
print(f"Отправление {mail.track} из {mail.from_address} в {mail.to_address}. Стоимость {mail.cost} рублей.")
