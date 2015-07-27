#from django.db import models

import math


def sigmoid(t):
    return 1 / (1 + math.exp(-4.924273 * t))


class Relaxed(Exception):
    THRESHOLD = 0.0005

    @classmethod
    def always(cls):
        raise cls


class Synapse(object):

    def __init__(self, axon, weight):
        self.weight = weight
        self.axon = axon

    @property
    def signal(self):
        return self.axon.activation * self.weight


class Neuron(object):

    def __init__(self):
        self.incoming_synapses = []
        self.activation = 0.0

    def fire(self):
        summed_values = sum(synapse.signal for synapse in self.incoming_synapses)
        activation = sigmoid(summed_values)
        if abs(self.activation - activation) < Relaxed.THRESHOLD:
            self.activation = activation
            raise Relaxed
        self.activation = activation


    def add_incoming(self, synapse):
        self.incoming_synapses.append(synapse)


class SensorNeuron(object):
    fire = Relaxed.always

    def __init__(self, value_function):
        self.value_function = value_function

    @property
    def activation(self):
        return self.value_function()


class BiasNeuron(object):
    fire = Relaxed.always
    activation = 1.0


class Network(object):

    def splice(self, axon, dendrite, weight):
        synapse = Synapse(axon, weight)
        dendrite.add_incoming(synapse)
