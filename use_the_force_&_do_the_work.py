train_mass = 22680
train_acceleration = 10
bomb_mass = 1
train_distance = 100

# Use the force:
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3 * 10 ** 8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Do the Work
def get_work(mass, acceleration, distance):
  return mass * acceleration * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
