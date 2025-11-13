import pyupbit

with open("key.txt") as f:
    access_key, secret_key = [line.strip() for line in f.readlines()]

upbit = pyupbit.Upbit(access_key, secret_key)

my_balance = upbit.get_balances()
for i in my_balance: print(i)