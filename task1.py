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
total = 0
for customer in customers:
  name = customer["name"]
  age = customer["age"]
  if age < 12:
    price = base_price * 0.5
  elif age >= 65:
    price = base_price * 0.7
  else:
    price = base_price
  print(name, "-", round(price, 2), "AZN")
  total += price
print("Total revenue:", round(total, 2), "AZN")
