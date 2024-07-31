from brownie import *

from functools import reduce
from operator import xor

def reduce_xor(digest: bytes, unit=4):
    return reduce(xor,[int(digest[i:i+unit].hex(), 16) for i in range(0, len(digest), unit)])

def scaling(input: int, input_range:int, output_range:int):
    return input*output_range//(input_range)

class KeccakGen:
    def __init__(self, state=web3.keccak(0)):
        self.state = state
        self.i = 0

    def gen16(self) -> int:
        if self.i == 32:
            self.i = 0
            self.state = web3.keccak(self.state)
        data = int(self.state[self.i:self.i+2].hex(), 16)
        self.i+=2
        return data

    def gen10000(self) -> int:
        return scaling(self.gen16(), 65536, 10000)

class LCG:
    def __init__(self, state=0):
        self.a = 1664525
        self.c = 1013904223
        self.m = 2 ** 32
        self.state = state % self.m

    def gen(self) -> int:
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def gen10000(self) -> int:
        self.state = (self.a * self.state + self.c) % self.m
        return scaling(self.gen(), self.m, 10000)