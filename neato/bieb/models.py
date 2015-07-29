import json

from neato.swamp import models as nn


class Bieb(object):

    def resurrect_from_filepath(self, path):
        with open(path) as json_file:
            genome = json.load(json_file)
        return self.network_from_json(genome)

    def __init__(self, input_function_mappings):
        self.input_functions = input_function_mappings

    def network_from_json(self, genome):
        neurons = [self._neuron(n) for n in genome['neurons']]
        lookup = {n.label: n for n in neurons}
        net = nn.Network(neurons)
        for synapse in genome['synapses']:
            # kp: todo: don't have disabled synapses in my model yet
            if synapse.get('disabled', False) != 'True':
                net.splice(lookup[synapse['axon']], lookup[synapse['dendrite']], synapse['weight'])
        return net

    def _neuron(self, definition):
        type = definition['type']
        label = definition['label']
        if type == 'Bias':
            return nn.BiasNeuron(label=label)
        if type == 'Sensor':
            input_function = self.input_functions[label]
            return nn.SensorNeuron(input_function, label=label)
        if type in ('Output', 'Hidden'):
            return nn.Neuron(label=label)
        assert False, "{} unknown neuron type".format(type)
