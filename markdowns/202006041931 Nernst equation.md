---
title: Nernst equation
author: Ramón Opazo
date: 04/06/2020
tags: [MCB80_1x, neurophysiology, neuroscience, membranePotential, equation]
description: The Nernst equation allows for the calculation of the net membrane potential given the relative concentration of a given ion on each side of the cell's membrane. When calculating the potential on an equilibrium state between diffusion and electrostatic forces on a single ion species we solve for the Nernst potential, and is denoted with the ion subscript.
image: 'https://images.unsplash.com/photo-1597816196853-9d15dfd9bb06?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1948&q=80'
---

The Nernst equation allows for the calculation of the net membrane potential given the _relative_ concentration of a given ion on each side of the cell's membrane. When calculating the potential on an equilibrium state between diffusion and electrostatic forces on a single ion species we solve for the **Nernst potential**, and is denoted with the ion subscript.

```latex
\displaystyle E_{ion} = \frac{RT}{zF} ln \frac{[ion]_{e}}{[ion]_{i}}
```

> for T in Kelvin, R = 8.314 J/K·mol (universal gas constant), F = 96,485 C/mol (Faraday's constant), ln: natural log, base e ~ 2.718, C: coulomb, [ion]e corresponds to the extracellular concentration of an ion, [ion]i thus to the intracellular concentration, and z: valence of the ion (in this cases can be approximated to the net charge of the ion, e.g. +1 in the case of K+, or +2 in the case of Ca+2).

Due to the fact that the Nernst potential is reached when the system is at equilibrium, it is also known as **equilibrium potential**. On a neuron, typically the **resting potential** (the membrane potential of the cell at rest) is about the same as the Nernst potential of $K^{+}$. Nevertheless, the resting potential is the result of the composite of the flow of multiple ions through channels plus the participation of ion pumps, whereas the Nernst potential only involves the equilibrium of a given ion.

Finally, the point at which the flux of ions reverse direction is called the **reversal potential**, and is usually used when talking about ion channels.

# Zettel

- §202006042106 ─ Cellular membrane driving force
- §202006052003 ─ Goldman–Hodgkin–Katz flux equation

# Links

- [Wikipedia » Nernst equation](https://en.wikipedia.org/wiki/Nernst_equation)
- [GitLab » Markdown guide](https://about.gitlab.com/handbook/markdown-guide/)
- [List of LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
