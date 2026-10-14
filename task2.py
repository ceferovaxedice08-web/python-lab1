from functools import reduce
customers = [
  {"name": "Gunes", "age": 12},
  {"name": "Ayten", "age": 89},
  {"name": "Murad", "age": 14},
  {"name": "Aynur", "age": 4},
  {"name": "Elsen", "age": 35},
  {"name": "Gulay", "age": 55},
  {"name": "Ali", "age": 65},
]
def ticket_price(age):
  base_price = 12
  if age < 12:
    return base_price * 0.5
  elif age >= 65:
    return base_price * 0.7
  else:
    return base_price
prices = list(map(lambda customer: ticket_price(customer["age"]), customers))
discounted = list(filter(lambda customer: ticket_price(customer["age"]) < 12, customers))
total = reduce(lambda x, y: x + y, prices)
print("Prices:", list(map(lambda p: round(p, 2), prices)))
print("Discounted:", list(map(lambda customer: customer["name"], discounted)))
print("Total revenue:", round(total, 2), "AZN")
