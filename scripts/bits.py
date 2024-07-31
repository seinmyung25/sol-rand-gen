from brownie import *
from web3 import Web3
import matplotlib.pyplot as plt

def count_bits(hex_data, bit_length):
    # Convert hex data to an integer
    num = int.from_bytes(hex_data, byteorder='big')

    # Initialize a list to count 1 bits at each position
    count_ones = [0] * bit_length

    # Count the 1 bits in each chunk of bit_length
    for i in range(256 // bit_length):
        chunk = (num >> (i * bit_length)) & ((1 << bit_length) - 1)
        for j in range(bit_length):
            if chunk & (1 << j):
                count_ones[j] += 1

    return count_ones

def main():
    bit_lengths = [256, 16, 8]

    # Initialize results storage
    results = {bit_length: [0] * bit_length for bit_length in bit_lengths}

    # Iterate from 0 to 999 (1000 times)
    for i in range(1000):
        keccak_result = web3.keccak(i)

        # Count bits for each bit length
        for bit_length in bit_lengths:
            count = count_bits(keccak_result, bit_length)
            results[bit_length] = [x + y for x, y in zip(results[bit_length], count)]

    for bit_length in bit_lengths:
        plt.figure(figsize=(10, 5))
        plt.bar(range(bit_length), results[bit_length], label=f'{bit_length}-bit', width=1)
        plt.title(f'Count of 1 Bits in {bit_length}-bit Segments')
        plt.xlabel('Bit Position')
        plt.ylabel('Count of 1 Bits')
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'plot/count_of_1_bits_{bit_length}_bit.png')
        # plt.show()
