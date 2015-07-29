from expecter import expect

from neato.lab.models import hand_crafted_xor
from neato.swamp.models import sigmoid, Clocked


Clocked.clock.start()

def simple_xor(s1, s2):
    nand = not(s1 and s2)
    orr = s1 or s2
    return nand and orr


class WhenTesting(object):

    def should_give_zero_for_zero_and_zero(self):
        expect(simple_xor(0,0)) == False

    def should_give_one_for_one_and_zero(self):
        expect(simple_xor(1,0)) == True

    def should_give_one_for_zero_and_one(self):
        expect(simple_xor(0,1)) == True

    def should_give_zero_for_one_and_one(self):
        expect(simple_xor(1,1)) == False


class WhenDefiningXorNetwork(object):

    def should_give_one_for_zero_and_one(self):
        expect(hand_crafted_xor(0, 1)) == 1

    def should_give_one_for_one_and_zero(self):
        expect(hand_crafted_xor(1, 0)) == 1

    def should_give_zero_for_zero_and_zero(self):
        expect(hand_crafted_xor(0, 0)) == 0

    def should_give_zero_for_one_and_one(self):
        expect(hand_crafted_xor(1, 1)) == 0


