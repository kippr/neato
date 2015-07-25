from expecter import expect

from neato.swamp.models import Neuron, sigmoid


class StubSynapse(object):

    def incoming(self, value):
        self.value = value
        return self

    def outgoing(self):
        return self.value


class WhenFiringNeurons(object):

    def should_pass_sum_of_incoming_to_sigmoid(self):
        incoming = StubSynapse().incoming(1.0)
        outgoing = StubSynapse()
        neuron = Neuron([incoming, incoming], [outgoing])
        neuron.fire()
        expect(outgoing.value) == sigmoid(2.0)
