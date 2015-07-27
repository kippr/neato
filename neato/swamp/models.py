import math


def sigmoid(t):
    return 1 / (1 + math.exp(-4.924273 * t))


RELAXED_THRESHOLD = 0.0005
RELAXED = 'Relaxed'

def always_relaxed(self):
    print '{} Activation: {}'.format(self.label, self.activation)
    return RELAXED


class Synapse(object):

    def __init__(self, axon, weight):
        self.weight = weight
        self.axon = axon

    @property
    def signal(self):
        return self.axon.activation * self.weight


class Labeled(object):
    _label = None

    def __init__(self, label=None):
        if label:
            self._label = label

    @property
    def label(self):
        return self._label if self._label else self.__class__.__name__


class Neuron(Labeled):

    def __init__(self, label=None):
        super(Neuron, self).__init__(label)
        self.incoming_synapses = []
        self.activation = 0.0

    def fire(self):
        summed_values = sum(synapse.signal for synapse in self.incoming_synapses)
        activation = sigmoid(summed_values)
        relaxed = RELAXED_THRESHOLD > abs(self.activation - activation)
        if relaxed:
            print '{} Activation: {}; Sum: {}'.format(self.label, activation, summed_values)
        self.activation = activation
        return RELAXED if relaxed else None

    def add_incoming(self, synapse):
        self.incoming_synapses.append(synapse)


class SensorNeuron(Labeled):
    fire = always_relaxed
    incoming_synapses = ()

    def __init__(self, value_function, label=None):
        super(SensorNeuron, self).__init__(label)
        self.value_function = value_function

    @property
    def activation(self):
        return self.value_function()


class BiasNeuron(Labeled):
    fire = always_relaxed
    incoming_synapses = ()
    activation = 1.0


class Network(object):

    def __init__(self, neurons, result_function=lambda *args: args):
        self.neurons = neurons
        self.result_function = result_function

    def splice(self, axon, dendrite, weight):
        synapse = Synapse(axon, weight)
        dendrite.add_incoming(synapse)

    def activate(self):
        excited_neurons = list(self.neurons)
        non_terminals = set(synapse.axon for neuron in self.neurons for synapse in neuron.incoming_synapses)
        outputs = [neuron for neuron in self.neurons if neuron not in non_terminals]
        while excited_neurons:
            excited_neurons = [neuron for neuron in excited_neurons if RELAXED != neuron.fire()]
        output_activations = tuple(o.activation for o in outputs)
        return self.result_function(*output_activations)
