# Adapted from "Computational Physics", M. Newman, Ex.10.1
from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,show,legend

# Constants
NTl = 0               # Number of thallium atoms
NPb = 0               # Number of lead atoms
NBi = 10000         # Number of bismuth atoms
NBi9 = 0              # Number of bismuth209 atoms
tau = 46*60        # Half life of bismuth in seconds
tautl = 2.2*60     # half life of thallium in seconds
taupb = 3.3*60*60  # half life of pb in seconds
h = 1.0               # Size of time-step in seconds
p = 1. - 2.**(-h/tau)   # Probability of decay in one step
ptl = 1. - 2.**(-h/tautl)   # Probability of decay in one step
ppb = 1. - 2.**(-h/taupb)   # Probability of decay in one step
tmax = 10000           # Total time

# Lists of plot points
tpoints = arange(0.0,tmax,h)
Tlpoints = []
Pbpoints = []
Bipoints = []
Bi9points = []

# Main loop
for t in tpoints:
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)
    Bipoints.append(NBi)
    Bi9points.append(NBi9)

    # Calculate the number of atoms that decay
    decay = 0
    for i in range(NBi):
        # note that random.random() returns a uniformly distributed number in the range [0,1]
        if random()<p:
            decay += 1
    if random()<.021:
        NTl += decay
    else:
        NPb += decay
    NBi -= decay

    print('Final Bismuth213 of step one:'+str(NBi))
    print('Final Thallium209 of step one:'+str(NTl))
    print('Final Lead209 of step one:'+str(NPb))

    decay = 0
    for i in range(NTl):
        if random()<ptl:
            decay +=1
    NTl -= decay
    NPb += decay

    print('Final Thallium209 of step two:'+str(NTl))
    print('Final Lead209 of step two:'+str(NPb))

    decay = 0
    for i in range(NPb):
        if random()<ppb:
            decay += 1
    NBi9 += decay
    NPb -= decay

print('Total Final Bismuth213:'+str(NBi))
print('Total Final Bismuth209:'+str(NTl))
print('Total Final Lead209:'+str(NPb))
print('Total Final Bismuth209:'+str(NBi9))
# Make the graph
plot(tpoints,Tlpoints,label='$^{209}$Tl')
plot(tpoints,Pbpoints,label='$^{209}$Pb')
plot(tpoints,Bipoints,label='$^{213}$Bi')
plot(tpoints,Bi9points,label='$^{209}$Bi')
xlabel("Time (s)")
ylabel("Number of atoms")
legend()
show()
