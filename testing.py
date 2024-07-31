def nomalize(rand: int, rand_max:int, range:int):
    return rand*range//(rand_max+1)

class KeccakGenerator:
    def __init__(self, state=web3.keccak(0)):
        self.state = state
        self.i = 0

    def gen(self) -> int:
        if self.i == 32:
            self.i=0
            self.state = web3.keccak(self.state)
        data = int(self.state[self.i:self.i+2].hex(), 16)
        self.i+=2
        return nomalize(data, 65536, 10000)