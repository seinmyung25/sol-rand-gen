from brownie import *
from web3 import Web3
import matplotlib.pyplot as plt

from scripts.bits import count_bits

def main():
    output_len = 256
    count_output_index = [0]*output_len

    # Iterate from 0 to 999 (1000 times)
    for i in range(100000):
        keccak_result = web3.keccak(i)
        count_output_index[sum(count_bits(keccak_result, output_len))] += 1
        # count 1bit index
    print(count_output_index)

    plt.figure(figsize=(10, 5))
    plt.bar(range(len(count_output_index)), count_output_index, width=1)
    plt.title(f'Count of bits of Keccak256 Ouput')
    plt.xlabel('Count of Number of 1 bits in Keccak256 Ouput')
    plt.ylabel('Number of 1 bits in Keccak256 Ouput')
    plt.tight_layout()
    plt.savefig(f'plot/hash out distributions.png')
    # plt.show()