# Ion optics

### Optimization of Twiss parameters to influence the emissivity of an ion beam

<p>Programs developed during an internship in ion optics to discover the notion of emissivity, Twiss parameters and "sigma" matrices for ion beams passing through different optical systems (drift, thin lens, Einzel lens, magnetic dipole, electrostatic quadrupole).</p>

<p>The parameters are given in **parameters.py**, which allows to change the values of the optical elements. The Twiss parameter "gamma" is calculated in **gamma.py**.</p>

<p>All sigma matrices have been calculated beforehand according to the transfer matrix of the different optical elements used. They are recorded in **sigmaMatrices.py**.</p>

<p>Finally, the ellipses are displayed thanks to the code coming from <a href="https://matplotlib.org/3.1.0/gallery/statistics/confidence_ellipse.html" title="this website">https://linuxhandbook.com/date-command/</a>, from which I took inspiration. </p>

<p>In order to visualize them, you just have to compile the file **confidence_ellipse.py**. You can modify the ellipses to display by copying the sigma matrix code from the **sigmaMatrices.py** file in this viewing program.</p>

