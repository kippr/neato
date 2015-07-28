from neato.swamp import models as nn

class Population(object):

    def __init__(self, input_functions, output_labels):
        def sensor(function):
            label = function.__name__
            return nn.SensorNeuron(function, label=label)
        inputs = [sensor(input) for input in input_functions] + [nn.BiasNeuron()]
        outputs = [nn.Neuron(label=label) for label in output_labels]
        self.genesis = nn.Network(inputs + outputs)
        for output in outputs:
            for input in inputs:
                self.genesis.splice(input, output, 1.0)

    def __getitem__(self, i):
        return self.genesis
