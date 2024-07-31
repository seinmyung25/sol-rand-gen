from brownie import *

from study.chisquare import test_uniform_distribution
from ..libs.prng import *
import matplotlib.pyplot as plt

import random

def main():
    seeding = 1000
    gen_count = 16*100

    data = [0]*10000

    for i in range(seeding):
        for j in range(gen_count):
            data[random.randint(0,9999)] +=1

    test_uniform_distribution(data)

    plt.figure(figsize=(10, 5))
    plt.bar(range(len(data)), data, width=1)
    plt.title(f'Count of 10000 Probability of Python Random')
    plt.xlabel('Probability Value')
    plt.ylabel('Count of Probability')
    plt.tight_layout()
    plt.savefig(f'plot/Count of 10000 Probability of Python Random.png')
    # plt.show()