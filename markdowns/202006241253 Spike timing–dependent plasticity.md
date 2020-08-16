# Spike timing–dependent plasticity
#MCB80_2x #neurophysiology #plasticity #model

A more nuanced model of Hebbian plasticity has been developed recently. This model, named **spike timing–dependent plasticity (STDP)** takes into account the timing of the excitation of the presynaptic neuron compared to the timing in the postsynaptic neuron. It makes a better picture representing the idea that neurons that fire together wire together, and that neurons out of sync lose their link.

STDPs shows two scenarios:

1. Presynaptic spikes that arrive a few tens of milliseconds _before_ the postsynaptic ones result in **potentiation**.
2. In the inverse case, a presynaptic spike that arrives a few tens of milliseconds _after_ the postsynaptic spike determines **depression**.

It is worth noting that the _closer_ the events are, the _stronger_ is the effect. Optimal potentiation occurs just before the postsynaptic spike happens. Strong depression results when the spike occurs in the opposite order.

![STDP model. Strengthtened synapses showed in red, depressed synapses in blue.](../img/f441849ee8e769ff0acb1dc25e928a92.png)

This system ensures **causality** of events (the firing of the pre and postsynaptic spikes), thus making causal associations more likely, and depressing non causal events. Neurons present random low level spike firing, so a system like the one presented can avoid creating associations when there is no _causal timing_.

For LTP caused by STDP there is the idea that **backpropagating** action potentials generated at the axon can arrive at the NMDA channels just in time for them to open and allow calcium into the neuron.

# Zettel

- §202006241629 ─ Nonsynaptic plasticity

# Links

- [Wikipedia » Spike–timing–dependent plasticity](https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity)