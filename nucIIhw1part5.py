from random import random,uniform
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics

N = 10000
b = 100.
m_bos = 200
p_bos = 1400

# simulate events
data = []
data_phi = []
polar_theta_points_list = []
E1_compare_points_list = []
for x in range(N):
    while 1:
        costheta_rest = uniform(-1,1)  # sample uniformly in cos(theta)
        phi_rest = uniform(0,2*3.1415)
        r1 = 2.*random()         # should we keep the event or not?
        if(r1 < costheta_rest):
            break
    data.append(costheta_rest)
    data_phi.append(phi_rest)

data_array = np.array(data)
data_phi_array = np.array(data_phi)

print(data_array)
for i in range(N):
    costheta_decay = data[i]
    theta_decay = math.acos(costheta_decay)
    px_decay = (m_bos/2)*math.sin(theta_decay)*math.sin(data_phi_array[i])
    py_decay = (m_bos/2)*math.sin(theta_decay)*math.cos(data_phi_array[i])
    pz_decay = (m_bos/2)*math.cos(theta_decay)

    E_lab = p_bos**2 + m_bos**2
    beta = (p_bos)/(E_lab)
    gamma = math.sqrt(1/(1-beta**2))

    p1z_lab = gamma*(pz_decay+beta*(m_bos/2))

    E1_lab = math.sqrt(px_decay**2 + py_decay**2 + p1z_lab**2)
    polar_theta = p1z_lab/E1_lab
    polar_theta_points_list.append(polar_theta)
    E1_compare_points_list.append(E1_lab)


max_cos=max(polar_theta_points_list)
max_E=max(E1_compare_points_list)
min_cos=min(polar_theta_points_list)
min_E=min(E1_compare_points_list)

probable_cos = Counter(polar_theta_points_list)
probable_E = Counter(E1_compare_points_list)
prob_cos=statistics.mean(polar_theta_points_list)
prob_E=statistics.mean(E1_compare_points_list)

print(max_cos)
print(max_E)
print(min_cos)
print(min_E)
print(prob_cos)
print(prob_E)

# draw the model curve, for comparison

plt.subplot(1,2,1)
plt.hist(polar_theta_points_list,bins=50, range=[-1,1])
plt.ylabel("Yield / 0.04")
plt.xlabel("cos(theta)")
plt.title("Polar Angle Distribution for p = 1400 MeV/c")

plt.subplot(1,2,2)
plt.hist(E1_compare_points_list, bins=50, range=[99,101])
plt.ylabel("Yield/0.04")
plt.xlabel("Energy in MeV")
plt.title("Energy Distribution for p = 1400 MeV/c")


plt.show()
