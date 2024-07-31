from brownie import *

from libs.prng import scaling

def main():
    print([scaling(i, 256, 100) for i in range(256)])