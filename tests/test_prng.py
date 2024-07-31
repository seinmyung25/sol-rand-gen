import pytest
from brownie import *

@pytest.fixture
def prng():
    return accounts[0].deploy(RandomGeneratorTest)

def test_initial_supply(prng):
    print(prng.address)
    assert accounts[0] == "0x66aB6D9362d4F35596279692F0251Db635165871"

def test_transfer(prng):
    print(prng.address)