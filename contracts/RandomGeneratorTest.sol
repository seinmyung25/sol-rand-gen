// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./RandomGenerator.sol";

contract RandomGeneratorTest {
    using Keccak256RG for Keccak256RG.KeccakRGState;
    using LinearCongretureGenerator for LinearCongretureGenerator.LCGState;

    function runKrng(bytes32 seed, uint64 yieldSize, uint256 count) public pure returns (uint256[] memory result10000s) {
        result10000s = new uint256[](count);
        Keccak256RG.KeccakRGState memory kst = Keccak256RG.init(seed, yieldSize);
        for(uint256 i; i<count; i++) {
            result10000s[i] = kst.yield10000();
        }
    }
    function runlcg(bytes32 seed, uint256 count) public pure returns (uint256[] memory result10000s) {
        result10000s = new uint256[](count);
        LinearCongretureGenerator.LCGState memory lst = LinearCongretureGenerator.init(seed);
        for(uint256 i; i<count; i++) {
            result10000s[i] = lst.yield10000();
        }
    }
}