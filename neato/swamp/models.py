#from django.db import models

import math


def sigmoid(t):
    return 1 / (1 + math.exp(-4.924273 * t))


class Neuron(object):

    def __init__(self, incoming_synapses):
        self.incoming_synapses = incoming_synapses
        self.activation = 0.0

    def fire(self):
        summed_values = sum(synapse.signal for synapse in self.incoming_synapses)
        self.activation = sigmoid(summed_values)
        return self.activation


class Synapse(object):

    def __init__(self, axon, weight):
        self.weight = weight
        self.axon = axon

    @property
    def signal(self):
        return self.axon.activation * self.weight
