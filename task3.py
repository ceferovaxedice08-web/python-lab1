customers = [
  {"name": "Gunes", "age": 12},
  {"name": "Ayten", "age": 89},
  {"name": "Murad", "age": 14},
  {"name": "Aynur", "age": 4},
  {"name": "Elsen", "age": 35},
  {"name": "Gulay", "age": 55},
  {"name": "Ali", "age": 65},
]
base_price = 12
def regular(age, base_price):
  if age < 12:
    return base_price * 0.5
  elif age >= 65:
    return base_price * 0.7
  else:
    return base_price
weekend = lambda age, base_price: base_price * 1.2
student_day = lambda age, base_price: base_price * 0.75
def sell_ticket(age, base_price, strategy):
  return strategy(age, base_price)
def sell_all(title, strategy):
  total = 0
  print(title)
  for customer in customers:
    price = sell_ticket(customer["age"], base_price, strategy)
    print(customer["name"], "-", round(price, 2), "AZN")
    total += price
  print("Total revenue:", round(total, 2), "AZN")
  print()
sell_all("Regular", regular)
sell_all("Weekend", weekend)
sell_all("Student day", student_day)
