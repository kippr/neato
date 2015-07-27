from expecter import expect

from neato.swamp.models import Network
from neato.swamp.models import Neuron
from neato.swamp.models import SensorNeuron
from neato.swamp.models import BiasNeuron
from neato.swamp.models import Synapse
from neato.swamp.models import Neuron
from neato.swamp.models import sigmoid
from neato.swamp.models import RELAXED


class StubSynapse(object):

    def __init__(self, signal):
        self.signal = signal


class StubNeuron(object):

    def __init__(self, activation):
        self.activation = activation


class WhenCalculatingActivation(object):

    def should_be_sigmoid_of_sum_of_incoming_values(self):
        incoming = StubSynapse(1.0)
        neuron = Neuron()
        neuron.add_incoming(incoming)
        neuron.add_incoming(incoming)
        neuron.fire()
        expect(neuron.activation) == sigmoid(2.0)


class WhenSynapsesTransmitSignals(object):

    def should_adjust_by_weight(self):
        synapse = Synapse(StubNeuron(10), 0.5)
        expect(synapse.signal) == 5.0


class WhenWorkingWithSensorNeurons(object):

    def should_pass_value_of_function_as_activation(self):
        function = lambda: 10.0
        neuron = SensorNeuron(function)
        expect(neuron.activation) == 10.0


class WhenWorkingWithBiasNeurons(object):

    def should_pass_constant_value_as_activation(self):
        neuron = BiasNeuron()
        expect(neuron.activation) == 1.0


class WhenCreatingNetwork(object):

    def should_set_links_up_on_splice(self):
        neuron1 = BiasNeuron()
        neuron2 = Neuron()
        weight = 0.5
        Network(()).splice(neuron1, neuron2, weight)
        neuron2.fire()
        expect(neuron2.activation) == sigmoid(0.5 * neuron1.activation)


class WhenActivatingNetwork(object):

    def should_fire_until_all_nodes_relaxed(self):
        sensor = SensorNeuron(lambda: 10)
        output = Neuron()
        net = Network((sensor, output))
        net.activate()
        expect((sensor.fire(), output.fire())) == (RELAXED, RELAXED)
