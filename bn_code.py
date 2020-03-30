import numpy as np
import matplotlib.pyplot as plt

# inisialisasi
d = 10 # Jarak antar garis parallel
l = 5 # Panjang jarum
N = np.arange(100,10100,100)
n_trial = 10

# iterasi
list_p = []
for n_needles in N:
    for trial in range(n_trial):
        Z = 0
        pi_trial = []
        for i in range(n_needles):
            #throw
            x = np.random.rand() * d
            theta = np.random.rand() * 90
            # condition
            if x <= l * np.cos(np.deg2rad(theta)): #degre konversi ke radian
                Z += 1
        pi = (2*l/d) * (n_needles/Z)
        pi_trial.append(pi)
    pi_avg = np.average(pi_trial)
    list_p.append(pi_avg)

#Print plot
# list_p
plt.plot(N, list_p, c='brown')
plt.scatter(N, list_p, c='brown', label='approximasi')
plt.axhline(y=np.pi, c='blue' , label='eksak')
plt.xlabel('Banyaknya needles')
plt.ylabel('$\pi$ value')
plt.legend()
plt.show()