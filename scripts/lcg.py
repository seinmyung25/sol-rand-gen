from brownie import *

from study.chisquare import test_uniform_distribution
from ..libs.prng import *
import matplotlib.pyplot as plt

def main():
    seeding = 1000
    gen_count = 16*100

    data = [0]*10000

    for i in range(seeding):
        lcg = LCG(reduce_xor(web3.keccak(i)))
        for j in range(gen_count):
            data[lcg.gen10000()] +=1

    test_uniform_distribution(data)

    plt.figure(figsize=(10, 5))
    plt.bar(range(len(data)), data, width=1)
    plt.title(f'Count of 10000 Probability of LCG')
    plt.xlabel('Probability Value')
    plt.ylabel('Count of Probability')
    plt.tight_layout()
    plt.savefig(f'plot/Count of 10000 Probability of LCG.png')
    # plt.show()