from expecter import expect

from neato.lab.models import hand_crafted_xor

class WhenDefiningXorNetwork(object):

    def should_give_one_for_zero_and_one(self):
        net = hand_crafted_xor(0, 1)
        expect(net.activate()) == 1

    def should_give_one_for_one_and_zero(self):
        net = hand_crafted_xor(1, 0)
        expect(net.activate()) == 1
