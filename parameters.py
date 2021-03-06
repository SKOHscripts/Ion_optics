'''
@file : parameters.py
@brief :  To simplify the calling of functions, all parameters are noted here. 
@author : Corentin MICHEL
creation : 20/07/2020
'''

import parameters_calculation
from math import *
import numpy as np

epsilon = 30  # Input emittance for the ion beam.
n_std = 2.2977  # n_std : float 	The number of standard deviations to determine the ellipse's radiuses. We take chi2=2.2977 for 68.3% (epsilon rms)
mu = 0, 0  # Two_dimensional mean (we take 0,0 by default, because that means that the beam is in average in the center of the ion gun).
scale = 1, 1  # Dimension we give to the beam.

#############################################################################
#
# Input signal
#

input_alpha = 0
input_beta = 2.3
input_gamma = parameters_calculation.gamma(input_alpha, input_beta, epsilon)

#############################################################################
#
# Drift parameters
#

drift_L = 0.424
drift_alpha = input_alpha
drift_beta = input_beta
drift_gamma = parameters_calculation.gamma(drift_alpha, drift_beta, epsilon)

#############################################################################
#
# Thin lens parameters
#

lens_f = 0.520
lens_alpha = input_alpha
lens_beta = input_beta
lens_gamma = parameters_calculation.gamma(lens_alpha, lens_beta, epsilon)

#############################################################################
#
# Thin lens + drift parameters
#

LensDrift_f = 0.520
LensDrift_L = 0.100
LensDrift_alpha = input_alpha
LensDrift_beta = input_beta
LensDrift_gamma = parameters_calculation.gamma(LensDrift_alpha, LensDrift_beta, epsilon)

#############################################################################
#
# Magnetic dipole parameters
#

dipoleMag_phi = 90
dipoleMag_p = 0.0260
dipoleMag_alpha = input_alpha
dipoleMag_beta = input_beta
dipoleMag_gamma = parameters_calculation.gamma(dipoleMag_alpha, dipoleMag_beta, epsilon)

#############################################################################
#
# Einzel lens parameters
#

einzel_L1 = 0.424
einzel_f = 0.520
einzel_L2 = 0.424
einzel_alpha = input_alpha
einzel_beta = input_beta
einzel_gamma = parameters_calculation.gamma(einzel_alpha, einzel_beta, epsilon)

#############################################################################
#
# Electrostatic quadrupole parameters
#
V0 = 900
V = 20000
R = 0.035
quadru_L = 0.100
quadru_drift_L = 0.100
quadru_alpha = input_alpha
quadru_beta = input_beta
quadru_gamma = parameters_calculation.gamma(quadru_alpha, quadru_beta, epsilon)
quadru_k = sqrt(parameters_calculation.k(V0, V, R))  # k [m(-1/2)]
print(f"k= {quadru_k} m(-1/2)")

#############################################################################
#
# Doublet parameters
#

V0 = 900
V = 20000
R = 0.035
doublet_L1 = 0.100
doublet_L2 = 0.040
doublet_L3 = 0.100
doublet_L4 = 0.100
doublet_alpha = input_alpha
doublet_beta = input_beta
doublet_gamma = parameters_calculation.gamma(doublet_alpha, doublet_beta, epsilon)
doublet_k1 = sqrt(parameters_calculation.k(V0, V, R))
doublet_k2 = sqrt(parameters_calculation.k(V0, V, R))

#############################################################################
#
# Triplet parameters
#

V0 = 900
V = 20000
R = 0.035
triplet_Lq1 = 0.100
triplet_Lq2 = 0.100
triplet_Lq3 = 0.100
triplet_Ld1 = 0.040
triplet_Ld2 = 0.040
triplet_Ld3 = 0.100
triplet_alpha = input_alpha
triplet_beta = input_beta
triplet_gamma = parameters_calculation.gamma(triplet_alpha, triplet_beta, epsilon)
triplet_k1 = sqrt(parameters_calculation.k(V0, V, R))
triplet_k2 = sqrt(parameters_calculation.k(V0, V, R))
triplet_k3 = sqrt(parameters_calculation.k(V0, V, R))
#############################################################################
#
# Voltage optimisation
#
optim_nb_points = 500
optim_min = 0
optim_max = 2000
optim_V = 20000
optim_R = 0.035
optim_drift_L = 0.050
optim_dist = 0.040  # distance between the quadrupoles
optim_drift_alpha = input_alpha
optim_drift_beta = input_beta
optim_drift_gamma = parameters_calculation.gamma(input_alpha, input_beta, epsilon)
optim_LensDrift_f = 0.520
optim_LensDrift_L = 0.100
optim_LensDrift_alpha = input_alpha
optim_LensDrift_beta = input_beta
optim_LensDrift_gamma = parameters_calculation.gamma(LensDrift_alpha, LensDrift_beta, epsilon)

#############################################################################
#
# Finding f
#

findingf_L1 = 0.600
findingf_L2 = 0.550
findingf_L3 = 1.100
findingf_L4 = 0.55
findingf_accuracy = 0.1
findingf_V = 3000
findingf_R = 0.035
findingf_eps = 5
findingf_alpha = 0
findingf_beta = 1.8
findingf_tocheck = np.linspace(-3000, 3000, 6001)
