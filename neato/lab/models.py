from neato.swamp.models import Network
from neato.swamp.models import SensorNeuron, BiasNeuron, Neuron

def hand_crafted_xor(i1, i2):
    s1, s2, bias = SensorNeuron(lambda: i1, 's1'), SensorNeuron(lambda: i2, 's2'), BiasNeuron('b1')
    nand = Neuron('nand')
    orr = Neuron('or')
    and_result = Neuron('and=result')
    net = Network((s1, s2, bias, nand, orr, and_result), lambda x: round(x))
    synapses = ((s1, nand, -1), (s1, orr, 1),
                (s2, nand, -1), (s2, orr, 1),
                (bias, nand, 1.5), (bias, orr, -1), (bias, and_result, -1.25),
                (nand, and_result, 1), (orr, and_result, 1))
    for axon, dendrite, weight in synapses:
        net.splice(axon, dendrite, weight)
    return net.activate()
