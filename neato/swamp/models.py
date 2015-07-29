import math



def sigmoid(t):
    return 1 / (1 + math.exp(-4.924273 * t))


RELAXED_THRESHOLD = 0.0005
RELAXED = 'Relaxed'


def always_relaxed(self):
    print '{} Activation: {}'.format(self.label, self.activation)
    return RELAXED


class Clocked(object):

    class SharedClock(object):

        def __init__(self, next_innovation_number=1):
            self._next_innovation_number = next_innovation_number

        @property
        def next_innovation_number(self):
            num = self._next_innovation_number
            self._next_innovation_number += 1
            return num


    clock = SharedClock()

    def __init__(self):
        super(Clocked, self).__init__()
        self.id = self.clock.next_innovation_number


class Synapse(Clocked):

    def __init__(self, axon, weight):
        super(Synapse, self).__init__()
        self.axon = axon
        self.weight = weight

    @property
    def signal(self):
        return self.axon.activation * self.weight


class Labeled(object):
    _label = None

    def __init__(self, label=None):
        super(Labeled, self).__init__()
        if label:
            self._label = label

    @property
    def label(self):
        return self._label if self._label else self.__class__.__name__


class Neuron(Labeled, Clocked):

    def __init__(self, label=None):
        super(Neuron, self).__init__(label=label)
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


class SensorNeuron(Labeled, Clocked):
    fire = always_relaxed
    incoming_synapses = ()

    def __init__(self, value_function, label=None):
        super(SensorNeuron, self).__init__(label=label)
        self.value_function = value_function

    @property
    def activation(self):
        return self.value_function()


class BiasNeuron(Labeled, Clocked):
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
