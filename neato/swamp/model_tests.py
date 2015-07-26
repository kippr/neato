from expecter import expect

from neato.swamp.models import Neuron
from neato.swamp.models import SensorNeuron
from neato.swamp.models import Synapse
from neato.swamp.models import Neuron
from neato.swamp.models import sigmoid


class StubSynapse(object):

    def __init__(self, signal):
        self.signal = signal


class StubNeuron(object):

    def __init__(self, activation):
        self.activation = activation


class WhenCalculatingActivation(object):

    def should_be_sigmoid_of_sum_of_incoming_values(self):
        incoming = StubSynapse(1.0)
        neuron = Neuron([incoming, incoming])
        neuron.fire()
        expect(neuron.activation) == sigmoid(2.0)


class WhenSynapsesTransmitSignals(object):

    def should_adjust_by_weight(self):
        synapse = Synapse(StubNeuron(10), 0.5)
        expect(synapse.signal) == 5.0


class WhenWorkingWithSensorNeurons(object):

    def should_pass_activation_thru_input_function(self):
        function = lambda: 10
        neuron = SensorNeuron(function)
        expect(neuron.activation) == 10
