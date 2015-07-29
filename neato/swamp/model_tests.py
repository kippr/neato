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

# tests all assume a running clock or else manage it themselves
Synapse.clock.start()

class WhenWantingToSeeSigmoidValues(object):

    def should_fail_this_test(self):
        def print_sigmoid(value):
            print '{}: {}'.format(value, sigmoid(value))
        print_sigmoid(-1)
        print_sigmoid(-0.5)
        print_sigmoid(0)
        print_sigmoid(0.5)
        print_sigmoid(1)
        assert True


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


class WhenTrackingInnovationNumbers(object):

    def should_count_neurons(self):
        Neuron.clock._next_innovation_number = 11
        expect(Neuron().id) == 11
        expect(Neuron().id) == 12

    def should_count_synapse_from_same_clock(self):
        Synapse.clock._next_innovation_number = 10
        neuron = Neuron()
        expect(neuron.id) == 10
        expect(Synapse(neuron, 10).id) == 11

    def should_be_able_to_manually_set_ids_only_while_clock_not_started(self):
        Synapse.clock.reset()
        neuron = Neuron(id=3)
        expect(neuron.id) == 3
        expect(Synapse(neuron, 10, id=7).id) == 7
        Synapse.clock.start()
        expect(Neuron().id) == 8
        with expect.raises(AssertionError):
            Neuron(id=3)


