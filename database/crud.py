import datetime
import config
import pydantic_models
import bit
from db import *

wallet = bit.PrivateKeyTestnet(config.test)  # наш кошелек готов и содержится в переменной wallet
print(f"Баланс: {wallet.get_balance()}")
print(f"Адрес: {wallet.address}")
print(f"Приватный ключ: {wallet.to_wif()}")
print(f"Все транзакции: {wallet.get_transactions()}")
outputs = [('muh9DYMTWXfPEd9zPnfvCS1yX8hPLbkE9e', 0.00001, "btc")]
transaction = wallet.send(outputs)
print(transaction)
