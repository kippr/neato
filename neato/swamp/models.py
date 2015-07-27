#from django.db import models

import math


def sigmoid(t):
    return 1 / (1 + math.exp(-4.924273 * t))


class Synapse(object):

    def __init__(self, axon, weight):
        self.weight = weight
        self.axon = axon

    @property
    def signal(self):
        return self.axon.activation * self.weight


class Neuron(object):

    def __init__(self, incoming_synapses):
        self.incoming_synapses = incoming_synapses
        self.activation = 0.0

    def fire(self):
        summed_values = sum(synapse.signal for synapse in self.incoming_synapses)
        self.activation = sigmoid(summed_values)


class SensorNeuron(object):

    def __init__(self, value_function):
        self.value_function = value_function

    @property
    def activation(self):
        return self.value_function()


class BiasNeuron(object):
    activation = 1.0
