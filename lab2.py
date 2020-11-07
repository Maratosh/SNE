#!/usr/bin/python3
# Factorial
def fac(x):
    if x == 1:
        return x
    else:
        return x*fac(x-1)
#######################
#(Walzenlage). Possible ways of selecting and ordering the rotors
#(Ringstellung). Possible ways to install rings around rotors.
#(Kenngruppen). Possible ways to position of the rotors in the machine.
#(Steckerverbindungen) Possible ways of connecting letters to each other with plugs.

r = 3 # rotors
n = 5 # unique rotors
w = 10 # wires
p = 26 # alphabet



Walzenlage = (fac(n)/fac(n-r))
Ringstellung = p ** (r - 1)
Kenngruppen = p ** r
Steckerverbindungen =  (fac(p)) / ( (fac(p - 2*w)) * (2**w) * (fac(w)) )

total = Walzenlage * Ringstellung * Kenngruppen * Steckerverbindungen

print('Possible ways of selecting and ordering the rotors', int(Walzenlage))
print('Possible ways to install rings around rotors', Ringstellung)
print('Possible ways to position of the rotors in the machine', Kenngruppen)
print('Possible ways of connecting letters to each other with plugs', Steckerverbindungen)
print('total probabilities',  total)

# the number of the plugboard cables at which the maximum number of probabilities of the Possible ways of connecting letters to each other
#for i in range (1, 15):
#    print(i, 'pairs', (fac(30)) / ( (fac(30 - 2* i)) * (2**i) * (fac(i)) ))
