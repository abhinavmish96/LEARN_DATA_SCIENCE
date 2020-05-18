def ground_ship(weight):
  flat = 20
  if weight <= 2:
    return weight*1.5 + flat
  elif weight > 2 and weight <= 6:
    return weight*3.0 + flat
  elif weight > 6 and weight <= 10:
    return weight*4.0 + flat
  else:
    return weight*4.75 + flat

cost = ground_ship(8.4)
print(cost)

def drone_ship(weight):
  flat = 0
  if weight <= 2:
    return weight*4.5 + flat
  elif weight > 2 and weight <= 6:
    return weight*9.0 + flat
  elif weight > 6 and weight <= 10:
    return weight*12.0 + flat
  else:
    return weight*14.25 + flat

cost1 = drone_ship(1.5)
print(cost1)