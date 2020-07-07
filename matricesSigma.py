from pylab import *
import numpy as np
from math import *

import calcul_gamma
import parameters

#############################################################################
#
# Drift
#
#


def Drift(L, a, b, g, eps):
    sigma = np.array([[b - 2 * L * a + L**2 * g + 2 * L * (-a + L**2 * g), -a + L * g],
                      [-a + L * g + L * g, g]])
    T = np.array([[1, L], [0, 1]])
    Ttr = T.transpose()
    return eps / math.pi * T.dot(sigma).dot(Ttr)


print("Drift: ", Drift(parameters.drift_L, parameters.drift_alpha,
                       parameters.drift_beta, parameters.drift_gamma, parameters.epsilon))


#############################################################################
#
# Thin lens
#
#
def Lens(f, a, b, g, eps):
    T = np.array([[1, 0], [-1 / f, 1]])
    Ttr = T.transpose()
    sigma = np.array(
        [[b, -1 / f * b - a],
         [-1 / f * b - a, 1 / f**2 * b + 2 / f * a + g]])
    return eps / math.pi * T.dot(sigma).dot(Ttr)


print("")
print("Lens: ", Lens(parameters.lens_f, parameters.lens_alpha,
                     parameters.lens_beta, parameters.lens_gamma, parameters.epsilon))


#############################################################################
#
# Thin lens + drift
#
#
# f=focale de la lentille, L=longueur du drift, a=alpha, b=beta, g=gamma, eps=epsilon
def LensDrift(f, L, a, b, g, eps):
    T = np.array([[1, 0], [-1 / f, 1]])
    Ttr = T.transpose()
    sigma = np.array(
        [[(b * (f - L)**2 + f * L * (f * g * L + 2 * a * (-f + L))) / (f**2), (-f * (b + a * f) + (b + f * (2 * a + f * g)) * L) / (f**2)],
         [(-f * (b + a * f) + (b + f * (2 * a + f * g)) * L) / (f**2), (b + 2 * a * f) / (f**2) + g]])
    return eps / math.pi * T.dot(sigma).dot(Ttr)


print("")
print("Lens + Drift: ", LensDrift(parameters.LensDrift_f, parameters.LensDrift_L, parameters.LensDrift_alpha,
                                  parameters.LensDrift_beta, parameters.LensDrift_gamma, parameters.epsilon))


#############################################################################
#
# Magnetic dipole
#
#
# phi=angle du dipôle, p=longueur, a=alpha, b=beta, g=gamma, eps=epsilon
def DipoleMag(phi, p, a, b, g, eps):
    T = np.array([[cos(phi), p * sin(phi)], [1 / p * sin(phi), cos(phi)]])
    Ttr = T.transpose()
    sigma = np.array(
        [[cos(phi)**2 * b - 2 * p * cos(phi) * sin(phi) * a + p**2 * sin(phi)**2 * g, -(cos(phi)**2 + sin(phi)**2) * a + cos(phi) * sin(phi) * (b / p + p * g)],
         [-(cos(phi)**2 + sin(phi)**2) * a + cos(phi) * sin(phi) * (b / p + p * g), 1 / p**2 * sin(phi)**2 * b - 2 / p * cos(phi) * sin(phi) * a + cos(phi)**2 * g]])
    return eps / math.pi * T.dot(sigma).dot(Ttr)


print("")
print("Magnetic dipole: ", DipoleMag(parameters.dipoleMag_phi, parameters.dipoleMag_p, parameters.dipoleMag_alpha,
                                     parameters.dipoleMag_beta, parameters.dipoleMag_gamma, parameters.epsilon))


#############################################################################
#
# Einzel lens
#
# Ici je vais la faire différemment pour m'éviter tous les calculs à la main
# Je vais décomposer au maximum et laisser python faire le produit matriciel
def Einzel(L1, f, L2, a, b, g, eps):
    T = np.array([[1 - L2 / f, L1 * (1 - L2 / f) + L2],
                  [-1 / f, -L1 / f + 1]])
    Ttr = T.transpose()
    Twiss_entrée = np.array([[b],
                             [a],
                             [g]])  # Twiss_sortie = A * Twiss_entrée

    A = np.array([[(1 - L2 / f)**2, -2 * (1 - L2 / f) * (L1 * (1 - L2 / f) + L2), (L1 * (1 - L2 / f) + L2)**2],
                  [(1 - L2 / f) * 1 / f, (1 - L2 / f) * (1 - L1 / f) - 1 / f *
                   (L1 * (1 - L2 / f) + L2), -(1 - L1 / f) * (L1 * (1 - L2 / f) + L2)],
                  [1 / f**2, -2 * (L1 * (1 - L2 / f) + L2) * (1 - L1 / f), (1 - L1 / f)**2]])

    Twiss_sortie = A.dot(Twiss_entrée)

    sigma = np.hstack([[Twiss_sortie[0], -Twiss_sortie[1]],
                       [Twiss_sortie[1], Twiss_sortie[2]]])

    return eps / math.pi * T.dot(sigma).dot(Ttr)


print("")
print("Einzel: ", Einzel(parameters.einzel_L1, parameters.einzel_f, parameters.einzel_L2, parameters.einzel_alpha,
                         parameters.einzel_beta, parameters.einzel_gamma, parameters.epsilon))