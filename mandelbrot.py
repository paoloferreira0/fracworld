import matplotlib.pyplot as plt
import numpy as np

def sequence(c,z=0):
    while True:
        yield z
        z=z**2+c


def complex_matrix(xmin,xmax,ymin,ymax,pixel_density):
    re=np.linspace(xmin,xmax,int((xmax-xmin)*pixel_density))
    im=np.linspace(ymin,ymax,int((ymax-ymin)*pixel_density))
    return re[np.newaxis,:]+im[:,np.newaxis]*1j

def is_stable(c,num_iterations):
    z=0
    for _ in range(num_iterations):
        z=z**2+c
    return abs(z)<=2

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=2021)

# Calcul direct de la stabilité
stable = is_stable(c, 20)

# Affichage sous forme d'image
plt.imshow(stable, cmap="binary", extent=(-2, 0.5, -1.5, 1.5))
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()