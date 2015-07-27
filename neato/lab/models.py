from neato.swamp.models import Network
from neato.swamp.models import SensorNeuron, BiasNeuron, Neuron

def hand_crafted_xor(i1, i2):
    s1, s2 = SensorNeuron(lambda: i1), SensorNeuron(lambda: i2)
    result = Neuron()
    bias = BiasNeuron()
    net = Network((s1, s2, bias, result), lambda x: round(x))
    net.splice(s1, result, 1.0)
    net.splice(s2, result, 1.0)
    net.splice(bias, result, -1.0)
    return net
