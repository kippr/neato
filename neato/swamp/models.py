#from django.db import models

import math


def sigmoid(t):
    return 1 / (1 + math.exp(-4.924273 * t))


class Neuron(object):

    def __init__(self, incoming, outgoing):
        self.incoming = incoming
        self.outgoing = outgoing

    def fire(self):
        summed_values = sum(synapse.outgoing() for synapse in self.incoming)
        activation = sigmoid(summed_values)
        for synapse in self.outgoing:
            synapse.incoming(activation)
