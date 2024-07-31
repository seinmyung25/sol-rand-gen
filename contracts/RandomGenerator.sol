// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

function reduceXOR32(bytes32 data) pure returns (bytes4) {
    return bytes4(reduceXOR(data, 32));
}

function reduceXOR(bytes32 data, uint256 out_bits) pure returns (bytes32) {
    require(256 % out_bits == 0);
    bytes32 tmp;
    for (uint256 bit_shift; bit_shift < 256; bit_shift += out_bits) {
        tmp ^= data << bit_shift;
    }
    return tmp;
}

function bytes32Keccak(bytes32 data) pure returns (bytes32) {
    assembly {
        mstore(0x00, data)
        data := keccak256(0x00, 0x20)
    }
    return data;
}

function scaling(uint256 input, uint256 inputRange, uint256 outputRange) pure returns (uint256) {
    unchecked {
        return input * outputRange / inputRange;
    }
}

library Keccak256RG {
    uint128 constant bits16Range = 2 ** 16;
    struct KeccakRGState {
        bytes32 seed;
        bytes32 weed;
        uint64 yieldSize;
        uint64 weedBitShifter;
    }

    function init(bytes32 seed, uint64 yieldSize) internal pure returns (KeccakRGState memory kst) {
        kst.seed = bytes32Keccak(seed);
        kst.weed = bytes32Keccak(kst.seed);
        require(256 % yieldSize == 0, "krng yieldSize");
        kst.yieldSize = yieldSize;
    }

    function updateWeed(KeccakRGState memory kst) internal pure {
        require(kst.weedBitShifter == 256 && kst.weed != bytes32(0));
        kst.weed = bytes32Keccak(kst.weed);
        kst.weedBitShifter = 0;
    }

    function yield16(KeccakRGState memory kst) internal pure returns (uint16 value) {
        require(kst.yieldSize == 16);
        unchecked {
            if (kst.weedBitShifter == 256) updateWeed(kst);
            value = uint16(bytes2(kst.weed << kst.weedBitShifter));
            kst.weedBitShifter += kst.yieldSize;
        }
    }

    function yield10000(KeccakRGState memory kst) internal pure returns (uint16) {
        return uint16(scaling(yield16(kst), bits16Range, 10000));
    }
}

library LinearCongretureGenerator {
    uint256 constant lcgMax = 2 ** 32;
    uint256 constant unit = 10000;

    struct LCGState {
        uint256 state;
    }

    function init(bytes32 seedLikeHash) internal pure returns (LCGState memory lcg) {
        unchecked {
            lcg.state = uint32(reduceXOR32(seedLikeHash));
        }
    }

    function init10000ByState(uint256 state) internal pure returns (LCGState memory lcg) {
        lcg.state = state;
    }

    function yield(LCGState memory lcg) internal pure returns (uint16) {
        unchecked {
            lcg.state = (1664525 * lcg.state + 1013904223) % lcgMax;
        }
        return uint16(scaling(lcg.state, lcgMax, unit));
    }

    function yield10000(LCGState memory lcg) internal pure returns (uint16) {
        unchecked {
            lcg.state = (1664525 * lcg.state + 1013904223) % lcgMax;
        }
        return uint16(scaling(lcg.state, lcgMax, unit));
    }
}