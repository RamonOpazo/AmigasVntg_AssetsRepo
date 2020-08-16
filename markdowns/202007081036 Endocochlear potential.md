# Endocochlear potential
#equation #equationSolution #audition #neurophysiology

Given the following table with ionic concentrations:

| **Ion** | **Endolymph** | **Perilymph** | **Permeability** |
|:-------:|:-------------:|:-------------:|:----------------:|
| $K^+$   | 150 mM        | 5 mM          | 1                |
| $Na^+$  | 1 mM          | 140 mM        | 100              |
| $Cl^-$  | 130 mM        | 115 mM        | 1                |

The calculation for the electric potential between the endolymph and perilymph (**endocochlear potential**) is as follows:

$$
\displaystyle V = \frac{RT}{F} ln \left( \frac{p_{K}[K]_{p} + p_{Na}[Na]_{p} + p_{Cl}[Cl]_{e}}{p_{K}[K]_{e} + p_{Na}[Na]_{e} + p_{Cl}[Cl]_{p}} \right)
$$

> where $[ion_p]$ is the ion concentration in the perilymph, $[ion_e]$ the ion concentration in the endolymph, and $p_{ion}$ is the permeability of a given ion. The rest of the terms are the same as in the GHK equation.

Python code is given below:

```python
from math import *
# Constants.
R = 8.314                   # universal gas constant
T = 300                     # temperature in Kelvin degrees (37 C°)
F = 96485                   # Faraday's constant
pK, pNa, pCl = 1, 100, 1    # permeablities
Ke, Nae, Cle = 150, 1, 130  # endolymph ionic concentration
Kp, Nap, Clp = 5, 140, 115  # perilymph ionic concentration
# Formula for endocochlear potential, in mV.
V = (R*T/F)*log((pK*Kp + pNa*Nap + pCl*Cle)/(pK*Ke + pNa*Nae + pCl*Clp))*1000
```

# Zettel

# Links

[Wikipedia » Endocochlear potential](https://en.wikipedia.org/wiki/Endocochlear_potential)