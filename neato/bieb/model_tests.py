from expecter import expect

from neato.bieb.models import Bieb
from neato.swamp.models import Clocked


Clocked.clock.start()


class WhenResurrecting(object):

    def should_work_with_steves_json_format(self):
        input_functions = {'S1': lambda: 0, 'S2': lambda: 1}
        net = Bieb(input_functions).resurrect_from_filepath('neato/bieb/xor_genome.json')
        expect(len(net.neurons)) == 5
        hidden = next(n for n in net.neurons if n.label == 'H164')
        expect([s.weight for s in hidden.incoming_synapses]) == [-0.30620646664352136, 0.7093529583312881]
        # kp: todo: error on my part of this network is not functional, rather was input?
        #expect(net.activate()) == 1
