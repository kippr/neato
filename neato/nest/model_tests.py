from expecter import expect
from neato.nest.models import Population

def spark(input_functions, number_of_outputs):
        population = Population(input_functions, number_of_outputs)
        return population[0]

class WhenStartingAfresh(object):

    def should_start_without_hidden_layer(self):
        input_functions = (lambda: 10, lambda: 5)
        output_labels = ('output_a', 'output_b')
        adam = spark(input_functions, output_labels)
        expect(len(adam.neurons)) == len(input_functions) + len(output_labels) + 1  # 1 bias

    def should_include_bias_neuron(self):
        adam = spark([lambda: 1], ['out'])
        expect('BiasNeuron' in [n.label for n in adam.neurons]) == True

    def should_be_fully_connected(self):
        input_functions = (lambda: 10, lambda: 5)
        output_labels = ('output_a', 'output_b')
        adam = spark(input_functions, output_labels)
        output_b = next(n for n in adam.neurons if n.label == 'output_b')
        expect(len(output_b.incoming_synapses)) == 3

    def should_default_weights_to_one(self):
        adam = spark([lambda: 1], ['out'])
        output = next(n for n in adam.neurons if n.incoming_synapses)
        expect(output.incoming_synapses[0].weight) == 1
