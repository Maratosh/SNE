# Factorial
def fac(x):
    if x == 1:
        return x
    else:
        return x*fac(x-1)
#-----------------------------------------------------------------------------------------
# Walzenlage (Rotor position)
# Ringstellung (Ping position) The relative position of the rotor and their internal wiring
# Steckerverbindungen Plug connections 

r = 3 # rotors
n = 5 # 50 unique rotors
w = 10 # wires
p = 26 # plugboard



Walzenlage = (fac(n)/fac(n-r))
Ringstellung = p ** (r - 1)
Steckerverbindungen =  (fac(p)) / ( (fac(p - 2*w)) * (2**w) * (fac(w)) )

t = Walzenlage * Ringstellung * Steckerverbindungen
