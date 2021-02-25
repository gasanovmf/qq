
# для коэф. силы тяги
ro = 1.2920
ca = 1
Si = 1
ri = 1

ci = 0.5*ro*ca*Si*ri**2 # коэф. силы тяги



m = 1
g = 9.8
dt = 0.001
apha = 0.6

Ix = 1
Iy = 1
Iz = 1

Im = 1
Ip = 1

l = 1

Iyzx = (Iy - Iz) / Ix
Izxy = (Iz - Ix) / Iy
Ixyz = (Ix - Iy) / Iz
