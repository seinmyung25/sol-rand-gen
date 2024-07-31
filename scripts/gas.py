from brownie import *

def main():
    con = accounts[0].deploy(RandomGeneratorTest)
    print("runKrng", con.runKrng.estimate_gas(ZERO_ADDRESS, 16, 100))
    print("runlcg", con.runlcg.estimate_gas(ZERO_ADDRESS, 100))