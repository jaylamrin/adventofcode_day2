import math, numpy as np

#with open("module_masses.txt", 'r') as f:
#    x = f.readlines()

fn = './module_masses.txt'
masses = np.loadtxt(fn)
tot_fuel, fuel = 0,0

for x in masses:
    y = math.floor(x/3) - 2
    while y > 0:
        fuel += y
        y = math.floor(y/3) - 2
        
    tot_fuel += fuel
    fuel = 0

# mass = input("Enter mass: ")
# fuel = math.floor(mass/3) - 2
print(tot_fuel)